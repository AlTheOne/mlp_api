from celery import shared_task, current_app
from django.core.mail import send_mail
from django.apps import apps
from django.utils import timezone

@shared_task
def send_email(subject, message, from_email, to, **kwargs):
    send_mail(subject, message, from_email, to, **kwargs)

def createDBTableCleanupTask(model_name, expiration_term, date_field='date_of_creation'):
    """
    Creates a new Celery task for deleting 'old' db table's rows.

    Takes next arguments:
    model_name - name of a model in format '[app name].[model name]', on which
        should be performed automatical cleanup.
    expiration_term - timedelta object, which sets a term of life of db-table's
        rows, in the end of what they should be removed.
    date_field - name of a datetime field in model, which will be used for
        evaluation of db-table's rows expiration time.
    """
    app_name, model_cls_name = model_name.split('.')

    # cause celery class-based task's constructor will only be called once per
    # process, it should be a new class for each new task, not a class instance

    class _TableCleanupTask(current_app.Task):
        name = '%s.tasks.%s_table_cleanup' % (app_name, model_cls_name.lower())
        _app_name = app_name
        _model_name = model_cls_name
        _model = None
        _field_name = date_field
        _period = expiration_term

        @property
        def model(self):
            # It takes the model first time when it's requirednot at the start
            # of a process for avoiding problems with imports in case when
            # model isn't ready yet.
            if self._model is None:
                self._model = apps.get_model(self._app_name, self._model_name)
            return self._model

        def run(self):
            time_floor = timezone.now() - self._period
            params = {self._field_name+'__lt': time_floor}
            self.model.objects.filter(**params).delete()

    current_app.tasks.register(_TableCleanupTask())
    return current_app.tasks[_TableCleanupTask.name]
