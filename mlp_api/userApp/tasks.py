import os
from celery import current_app
from django.conf import settings
from django.utils.text import get_valid_filename
from PIL import Image
from userApp.utils import get_thumbnail_name
from commonApp.utils import remove_directory_files

class UserAvatarProcessing(current_app.Task):
    """
    Class-based task for handling user's avatar download event.
    Initializes with two arguments: avatar size and avatar's thumbnail size,
    both arguments are tuples with two elements: width, height .
    """
    name = 'userApp.tasks.process_user_avatar'

    def __init__(self, avatar_size, avatar_thumbnail_size):
        self.avatar_size = avatar_size
        self.avatar_thumbnail_size = avatar_thumbnail_size

    def _make_user_avatar(self, avatar, avatar_file):
        # Resizing given user's picture:
        correct_image = Image.open(avatar_file).resize(self.avatar_size)
        correct_image.save(avatar, 'JPEG')
        # Creating thumbnail:
        thumbnail = get_thumbnail_name(avatar)
        correct_image.thumbnail(self.avatar_thumbnail_size)
        correct_image.save(thumbnail, 'JPEG')

    def run(self, img_path=None, img_file=None, img_old_path=None):
        """
        The task takes next arguments:
        path, old_path - path, relative to MEDIA_ROOT,
            to corresponding new and old avatar images.
        file - a new avatar image file, uploaded by user.
        """

        if img_old_path is not None:
            old_avatar = os.path.join(settings.MEDIA_ROOT, img_old_path)
            avar_dir = os.path.dirname(old_avatar)
            if os.path.isdir(avar_dir):
                remove_directory_files(avar_dir)
        if img_path is not None and img_file is not None:
            avatar = os.path.join(settings.MEDIA_ROOT, img_path)
            self._make_user_avatar(avatar, img_file)

    @classmethod
    def initialize(cls, avatar_size, avatar_thumbnail_size):
        current_app.tasks.register(cls(
            avatar_size=avatar_size,
            avatar_thumbnail_size=avatar_thumbnail_size
        ))
        return current_app.tasks[cls.name]
