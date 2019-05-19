from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars

from pytils.translit import slugify
from tinymce.models import HTMLField


class Page(models.Model):
    """Static page make up from selected blocks"""

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
        unique=True,
        help_text=_("At most 128 characters, allowed characters:'-_a-z0-9'.")
    )
    seo_description = models.CharField(
        _('seo description'),
        max_length=100,
        help_text=_("At most 100 characters.")
    )
    blocks_content = models.ManyToManyField(
        'BlockPage',
        verbose_name=_('Blocks of content')
    )
    data_of_created = models.DateTimeField(
        _('data of create'),
        auto_now_add=True,
        auto_now=False
    )
    data_of_updated = models.DateTimeField(
        _('data of updated'),
        auto_now_add=False,
        auto_now=True
    )
    is_activate = models.BooleanField(
        _('is activate'),
        default=True
    )

    class Meta:
        verbose_name = _("static page")
        verbose_name_plural = _("static pages")

    def save(self, *args, **kwargs):
        """
        If the field is not filled when saving, it is automatically
        filled with the page header of the page
        """
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def short_title(self):
        """
        The function of limiting the length of the page header to
        50 characters
        """
        return truncatechars(self.title, 50)

    def __str__(self):
        return self.title


class BlockPage(models.Model):
    """Blocks that make up page content page"""

    title = models.CharField(
        _('title'),
        max_length=255,
        unique=True,
        help_text=_("At most 255 characters.")
    )
    content = HTMLField(_('content of block'))
    data_of_created = models.DateTimeField(
        _('data of create'),
        auto_now_add=True,
        auto_now=False
    )
    data_of_updated = models.DateTimeField(
        _('data of updated'),
        auto_now_add=False,
        auto_now=True
    )

    def __str__(self):
        return self.title