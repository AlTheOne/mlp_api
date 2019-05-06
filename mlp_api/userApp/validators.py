from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from PIL import Image

@deconstructible
class ImageSizeValidator:
    """
    Takes width and height in pixels for comparing with image size.
    Creates validator for an ImageField.
    """
    message = _(
        "Ensure that image size is equal to " +
        "%(limit_width)sx%(limit_height)s pixels."
    )
    code = "limit_image_size"

    def __init__(self, limit_width, limit_height, message=None, code=None):
        self.limit_width = limit_width
        self.limit_height = limit_height

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        try:
            size = value.width, value.height
        except ValueError:
            # Image field with image type 'image/x-icon' produces an ValueError
            # with message: 'buffer is not large enough' each time
            # when you attempt to read its 'width/height' property.
            size = Image.open(value.file).size

        limit_size = self.limit_width, self.limit_height

        if self.compare_size(size, limit_size):
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    'limit_width': self.limit_width,
                    'limit_height': self.limit_height
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.min_width == other.min_width and
            self.min_height == other.min_height and
            self.message == other.message and
            self.code == other.code
        )

    def compare_size(self, current_size, limit_size):
        width, height = current_size
        limit_width, limit_height = limit_size
        return not (width == limit_width and height == limit_height)

@deconstructible
class MinImageSizeValidator(ImageSizeValidator):
    message = _(
        "Ensure that image size is not less than " +
        "%(limit_width)sx%(limit_height)s pixels."
    )
    code = "min_image_size"

    def compare_size(self, current_size, min_size):
        width, height = current_size
        min_width, min_height = min_size
        return width < min_width or height < min_height

@deconstructible
class MaxImageSizeValidator(ImageSizeValidator):
    message = _(
        "Ensure that image size is not more than " +
        "%(limit_width)sx%(limit_height)s pixels."
    )
    code = "max_image_size"

    def compare_size(self, current_size, max_size):
        width, height = current_size
        max_width, max_height = max_size
        return width > max_width or height > max_height
