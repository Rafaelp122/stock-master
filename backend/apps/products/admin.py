from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Mostrando o 'code' que criamos para o SKU
    list_display = ("name", "code", "created_at")
    search_fields = ("name", "code")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",  # SKU primeiro é mais profissional
        "name",
        "category",
        "price",
        "stock_quantity",
        "display_qrcode",  # Miniatura na lista
    )
    # qrcode_image fica escondido, display_qrcode_large mostra a imagem grande na edição
    readonly_fields = ("sku", "display_qrcode_large")
    search_fields = ("name", "sku")
    list_filter = ("category",)

    def display_qrcode(self, obj):
        if obj.qrcode_image:
            return mark_safe(
                f'<img src="{obj.qrcode_image.url}" width="50" height="50" style="border-radius: 4px;" />'  # noqa
            )
        return "Gerando..."

    display_qrcode.short_description = "QR Code"

    def display_qrcode_large(self, obj):
        if obj.qrcode_image:
            return mark_safe(
                f'<img src="{obj.qrcode_image.url}" width="200" height="200" />'
            )
        return "O QR Code será gerado automaticamente ao salvar."

    display_qrcode_large.short_description = "Visualização do QR Code"
