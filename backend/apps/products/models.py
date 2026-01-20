import unicodedata
from io import BytesIO

import qrcode
import uuid6
from django.core.files import File
from django.db import models, transaction
from django.utils.text import slugify
from django.utils.timezone import now


def normalize_sku_part(text):
    """Remove acentos e caracteres especiais, garantindo um SKU seguro."""
    if not text:
        return "GEN"  # Generico se falhar
    # Normaliza para decompor caracteres
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Remove espaços e caracteres não alfanuméricos, deixa em caixa alta
    return slugify(text).replace("-", "").upper()[:3]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(blank=True, default="", verbose_name="Descrição")
    # Campo 'code' obrigatório para o padrão do SKU
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Código da Categoria",
        help_text="Abreviação de 3 letras (Ex: ELE, VEST, INF)",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"{self.name} ({self.code})"


class SkuSequence(models.Model):
    """Garante a unicidade numérica e evita concorrência."""

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    last_number = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("category", "year")
        verbose_name = "Sequência de SKU"

    def __str__(self):
        return f"{self.category.code} - {self.year}"


class Product(models.Model):
    # UUIDv7: Ordenado pelo tempo, excelente para indexação de banco de dados
    id = models.UUIDField(primary_key=True, default=uuid6.uuid7, editable=False)
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(blank=True, default="", verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Estoque")
    min_stock = models.PositiveIntegerField(default=5)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Categoria",
    )

    # SKU: Pode ser preenchido manualmente ou gerado automaticamente
    sku = models.CharField(max_length=50, unique=True, blank=True, db_index=True)
    qrcode_image = models.ImageField(
        upload_to="qrcodes/", blank=True, null=True, editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Imutabilidade: Só gera se for um novo registro (adding)
        is_new = self._state.adding

        if is_new:
            # Garante o ID para o QR Code
            if not self.id:
                self.id = uuid6.uuid7()

            # Geração Segura de SKU
            if not self.sku:
                year = now().year
                with transaction.atomic():
                    # select_for_update() coloca um "cadeado" na linha até o save acabar
                    seq, _ = SkuSequence.objects.select_for_update().get_or_create(
                        category=self.category,
                        year=year,
                    )
                    seq.last_number += 1
                    seq.save()

                    prefixo = normalize_sku_part(self.category.code)
                    self.sku = f"{prefixo}-{year}-{seq.last_number:04d}"
            else:
                self.sku = self.sku.upper().strip()

        # Geração do QR Code (Só na criação)
        if is_new and not self.qrcode_image:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(str(self.id))  # QR aponta para o UUID imutável
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            filename = f"qr-{self.sku}.png"
            self.qrcode_image.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)
