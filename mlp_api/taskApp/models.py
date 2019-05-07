from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
# Create your models here.
from projectApp.models import Project
from userApp.models import User


class Task (models.Model):

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
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('user')
    )
    # executor = models.ForeignKey(
    #         User,
    #         null=True,
    #         on_delete=models.PROTECT,
    #         verbose_name=_('executor')
    #     )
    task_status = models.ForeignKey(
        'StatusTask',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_('task status')
    )
    date_of_created = models.DateTimeField(
        _('date of creation'),
        auto_now_add=False,
        auto_now=True
    )
    date_of_updated = models.DateTimeField(
        _('date of update'),
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

    def __str__(self):
        return "'%s' task." % self.title

class StatusTask (models.Model):

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

    title = models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name = _("label task")
        verbose_name_plural = _("label tasks")

    def __str__(self):
        return self.title

