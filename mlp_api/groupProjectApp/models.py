from django.db import models
from django.utils.translation import ugettext_lazy as _
from userApp.models import User
from projectApp.models import Project


class Group(models.Model):
    """Groups created in the project to separate participants."""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="rel_group_proj",
        verbose_name=_("project")
    )
    is_main = models.BooleanField(
        _('main'),
        default=False,
        help_text=_("this group will be main")
    )
    name = models.CharField(
        _('name'),
        max_length=127,
        help_text=_("At most 127 characters.")
    )
    participants = models.ManyToManyField(
        User,
        related_name="rel_group_user",
        verbose_name=_("participants")
    )

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name