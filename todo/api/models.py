from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    PENDING = 'P'
    ONGOING = 'O'
    DONE = 'D'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ONGOING, 'Ongoing'),
        (DONE, 'Done'),
    ]

    body = models.CharField(max_length=250)
    due_date = models.DateTimeField(blank=True, null=True)
    repeat = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='tasks')
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=PENDING)
    category = models.ForeignKey(
        Category, models.CASCADE, related_name='tasks', blank=True, null=True)

    # TODO/OPTIONAL: attachements

    def __str__(self):
        return self.body


class TaggedTask(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='task')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL,
                            related_name='tag', null=True, blank=True)


class Reminder(models.Model):
    task = models.ForeignKey(Task, models.CASCADE, related_name='reminders')
    date = models.DateTimeField()

    def __str__(self):
        return self.name
