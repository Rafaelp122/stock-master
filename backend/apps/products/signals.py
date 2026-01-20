import logging
import os

from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Product


logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Apaga o arquivo do QR Code do armazenamento físico
    quando o registro do produto é removido do banco.
    """
    if instance.qrcode_image:
        try:
            if os.path.isfile(instance.qrcode_image.path):
                os.remove(instance.qrcode_image.path)
        except Exception as e:
            # Log do erro sem interromper a deleção do objeto
            logger.error(
                "Erro ao deletar arquivo QR Code do produto %s: %s",
                instance.sku,
                e,
                exc_info=True,
            )
