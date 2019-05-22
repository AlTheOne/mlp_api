from io import BytesIO
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    FileExtensionValidator
)
from django.utils.text import slugify
from tinymce.models import HTMLField
from projectApp.tasks import process_project_preview
from projectApp.utils import get_project_preview_path
from utils.validators import FileSizeValidator

class Project(models.Model):
    """Represents project, published on the web-site."""

    title = models.CharField(
        _('title'),
        max_length=255,
        unique=True,
        help_text=_("At most 255 characters.")
    )
    slug = models.SlugField(
        _('slug'),
        max_length=128,
        blank=True,
        null=True,
        unique=True,
        help_text=_("At most 128 characters, allowed characters:'-_a-z0-9'.")
    )
    preview = models.ImageField(
        _('preview'),
        upload_to=get_project_preview_path,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']),
            FileSizeValidator(2.5 * 1024 * 1024)
        ],
        blank=True,
        null=True
    )
    short_description = models.TextField(_('short description'))
    full_description = HTMLField(_('full description'))
    number_of_people = models.PositiveSmallIntegerField(
        _('number of people'),
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        help_text=_("Positive integer in range 1 to 1000 inclusive.")
    )
    date_of_created = models.DateTimeField(
        _('date of creation'),
        auto_now_add = True,
        auto_now = False
    )
    date_of_updated = models.DateTimeField(
        _('date of update'),
        auto_now_add = False,
        auto_now = True
    )
    date_of_end = models.DateTimeField(_('date of end'), null=True, blank=True)
    is_active = models.BooleanField(_('is active'), default=True)

    status = models.ForeignKey(
        'Status',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('status')
    )
    technologies = models.ManyToManyField(
        'Technology',
        related_name='projects',
        verbose_name=_('programming languages/technologies')
    )

    class Meta:
        verbose_name = _("enrolled project")
        verbose_name_plural = _("enrolled projects")

    def _prepare_preview_update(self):
        """
        Checks if there is some difference between present and old images, like:
        old was replaced or removed, or old doesn't exist and a new was passed.
        Returns dictionary with parameters for image processing task.
        (dictionary will be empty if nothing of told above will happen).
        """

        old_qs = Project.objects.filter(pk=self.id)
        old_preview = old_qs.first().preview if old_qs.exists() else None
        preview_process_params = {}
        if self.preview != old_preview:
            if old_preview:
                preview_process_params.update({'img_old_path': old_preview.name})
            if self.preview:
                img_file = self.preview.file.file
                # At the moment we don't need to save the whole uploaded image
                # cause it will do asynchronous celery worker
                # so let's put an empty byte stream instead actual image file:
                self.preview.save(self.preview.name, BytesIO(), save=False)
                preview_process_params.update({
                    'img_path': self.preview.name,
                    'img_file': img_file
                })

        return preview_process_params

    def save(self, *args, **kwargs):
        # Update slug field, if it's empty - write slugified title there:
        self.slug = self.slug.lower() if self.slug else slugify(self.title)
        # Prepare preview update:
        preview_process_params = self._prepare_preview_update()

        super().save(*args, **kwargs)

        if preview_process_params:
            process_project_preview.delay(**preview_process_params)

    def __str__(self):
        return "'%s' project." % self.title

class Technology(models.Model):
    """
    Represents programming language or technology,
    used in some project. Many technologies can be attached to a project,
    so it has many to many relationship with Project model.
    """

    title = models.CharField(
        _('title'),
        max_length=50,
        unique=True,
        help_text=_("At most 50 characters.")
    )
    slug = models.SlugField(
        _('slug'),
        max_length=50,
        unique=True,
        null=True,
        help_text=_("At most 50 characters, allowed characters:'-_a-z0-9'.")
    )

    class Meta:
        verbose_name = _("project's technology")
        verbose_name_plural = _("project's technologies")

    def save(self, *args, **kwargs):
        """
        Before storing data in database,
        converts slug string to lower case.
        """

        self.slug = self.slug.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Status(models.Model):
    """
    Represents status of some project.
    (for ex. 'active', 'complete')
    """

    title = models.CharField(
        _('title'),
        max_length=16,
        unique=True,
        help_text=_("At most 16 characters.")
    )

    class Meta:
        verbose_name = _("project's status")
        verbose_name_plural = _("project's statuses")

    def __str__(self):
        return "Status: '%s'." % self.title
