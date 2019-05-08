from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from colorfield.fields import ColorField
# Create your models here.
from projectApp.models import Project
from userApp.models import User


class Task (models.Model):
    """Creation of tasks for the current project"""
    title = models.CharField(
        _('title'),
        max_length=255,
        unique=True,
        help_text=_("At most 255 characters.")
    )
    task_description = HTMLField(
        _('task description')
    )
    task_project = models.ForeignKey(
        Project,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('project')
    )
    task_current = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('current task')
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user',
        verbose_name=_('user')
    )
    executor = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='executor',
        verbose_name=_('executor')
    )
    task_status = models.ForeignKey(
        'StatusTask',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('task status')
    )
    task_label = models.ForeignKey(
        'LabelTask',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('task label')
    )
    date_of_created = models.DateTimeField(
        _('date of creation'),
        auto_now_add=True,
        auto_now=False,
    )
    date_of_updated = models.DateTimeField(
        _('date of update'),
        auto_now_add=False,
        auto_now=True,
    )

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def __str__(self):
        return self.title

class StatusTask (models.Model):
    """Statuses of tasks which are now in the project"""
    title = models.CharField(
        _('title'),
        max_length=50,
        unique=True,
        help_text=_("At most 50 characters.")
    )

    class Meta:
        verbose_name = _("status task")
        verbose_name_plural = _("status tasks")

    def __str__(self):
        return self.title

class LabelTask (models.Model):
    """Job tags that are currently in the project"""
    title = models.CharField(
        _('title'),
        max_length=50,
        unique=True,
        help_text=_("At most 50 characters.")
    )
    color = ColorField(
        default='#ffffff'
    )
    task_project = models.ForeignKey(
        Project,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('project')
    )

    class Meta:
        verbose_name = _("label task")
        verbose_name_plural = _("label tasks")

    def __str__(self):
        return self.title

