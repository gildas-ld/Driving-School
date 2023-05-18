import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import OrderItem, Stock

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=OrderItem)
def update_stock(sender, instance, **kwargs):
    if kwargs["raw"]:
        return
    ref_id = instance.reference.id
    count = instance.count
    bar_id = instance.bar_id
    try:
        stock = Stock.objects.get(bar_id=bar_id, reference_id=ref_id).stock
        if stock is not None:
            if stock - count >= 0:
                stock = stock - count
                logger.warning(
                    f"Updated stock for reference : {ref_id} in bar : {bar_id} to {stock - count}"
                )
                if 0 < stock - count <= 2:
                    logger.warning(
                        f"Low stock for reference : {ref_id} in bar : {bar_id} : ({stock - count})"
                    )
            else:
                logger.warning(
                    f"Not enough stock for reference : {ref_id} in bar : {bar_id}, missing : ({stock - count})"
                )
        else:
            logger.warning(f"No stock for reference : {ref_id} in bar : {bar_id}")
    except Stock.DoesNotExist:
        logger.warning(f"No stock for reference : {ref_id} in bar : {bar_id}")
