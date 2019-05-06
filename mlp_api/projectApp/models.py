from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    FileExtensionValidator
)
from django.utils.text import slugify

from tinymce.models import HTMLField
from projectApp.validators import FileSizeValidator


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
        upload_to='projectApp/previews/',
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

    def save(self, *args, **kwargs):
        # Update slug field, if it's empty - write slugified title there:
        self.slug = self.slug.lower() if self.slug else slugify(self.title)

        # Check preview, if it has updated, remove old image:
        try:
            old_self = Project.objects.get(id=self.id)
            if (not self.preview) or self.preview != old_self.preview:
                old_self.preview.delete(save=False)
        except:
            # If it's a new project or a first preview, just don't do nothing:
            pass

        super().save(*args, **kwargs)

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
