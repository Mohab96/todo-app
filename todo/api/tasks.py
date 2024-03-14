from datetime import datetime
from celery import shared_task
from api.models import Reminder
from django.conf import settings
from notificationapi_python_server_sdk import notificationap


@shared_task
def send_notifications():
    reminders = Reminder.objects.all()

    for reminder in reminders:
        if reminder.date == datetime.datetime.now():
            user = reminder.task.user
            # send notification for the user here ...
