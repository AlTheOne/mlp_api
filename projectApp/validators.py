from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

@deconstructible
class FileSizeValidator:
    """
    Takes maximum size, allowed for a file, in bytes.
    Creates validator for a FileField.
    """
    message = _(
        "Ensure that file size are less than %(max_size)s %(prefix)sBytes."
    )
    code = 'limit_file_size'

    _decimal_prefixes = ('k', 'M', 'G')


    def __init__(self, max_size, message=None, code=None):
        self.max_size = max_size
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(
                self.message,
                code=self.code,
                params=self._get_pretty_size_params()
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.max_size == other.max_size and
            self.message == other.message and
            self.code == other.code
        )

    def _get_pretty_size_params(self):
        """
        Returns a dictionary with message parameters
        (max_size, prefix) as keys, and values, depends on
        maximum allowed bytes for a file.
        """
        max_size = self.max_size
        prefix = ''

        options_quantity = len(FileSizeValidator._decimal_prefixes)
        for i in range(options_quantity, 0, -1):
            base = 1024 ** i
            if self.max_size >= base:
                max_size /= base
                prefix = FileSizeValidator._decimal_prefixes[i - 1]
                break

        return {'max_size':round(max_size, 2), 'prefix':prefix}
