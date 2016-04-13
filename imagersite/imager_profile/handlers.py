from django.db.models.signals import post_save, pre_delete
import logging
from django.conf import settings
from django.dispatch import receiver
from imager_profile.models import ImagerProfile


logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ensure_imager_profile(sender, **kwargs):
    if kwargs.get('created', False):
        try:
            new_profile = ImagerProfile(user=kwargs['instance'])
            new_profile.save()
        except ValueError:
            msg = 'unable to create image profile for {}'.format(sender)
            logger.error(msg.format(kwargs['instance']))


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_imager_profile(sender, **kwargs):
    try:
        kwargs['instance'].profile.delete()
    except AttributeError:
        msg = (
            "Instance not deleted. Doesn't exist?"
        )
        logger.warn(msg.format(kwargs['instance']))
