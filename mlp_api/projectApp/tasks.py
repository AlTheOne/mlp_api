import os
from celery import shared_task
from django.conf import settings
from PIL import Image


@shared_task(serializer='pickle')
def process_project_preview(img_path=None, img_file=None, img_old_path=None):
    """
    The task takes next arguments:
    img_path, img_old_path - path, relative to MEDIA_ROOT,
        to corresponding new and old preview images.
    img_file - a new profile's preview image file, uploaded by user.
    """
    if img_old_path is not None:
        old_preview_abs_path = os.path.join(settings.MEDIA_ROOT, img_old_path)
        try:
            os.remove(old_preview_abs_path)
        except FileNotFoundError:
            pass
    if img_path is not None and img_file is not None:
        preview_abs_path = os.path.join(settings.MEDIA_ROOT, img_path)
        Image.open(img_file).save(preview_abs_path, 'JPEG')
