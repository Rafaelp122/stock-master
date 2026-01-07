import uuid
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Quantidade em Estoque")
    min_stock = models.PositiveIntegerField(default=5) # Para alertas
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products",
        verbose_name="Categoria"
    )
    # Este campo será usado para gerar o QR Code
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU/Código")
    qrcode_image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name
