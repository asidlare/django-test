from django.db import models
from core.models.taskuser import TaskUser
from core.models.utils import TimeStampedModel


class Task(TimeStampedModel):
    STATUS_PENDING = 'P'
    STATUS_STARTED = 'S'
    STATUS_COMPLETED = 'C'
    DEFAULT_STATUS = STATUS_PENDING

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_STARTED, 'Started'),
        (STATUS_COMPLETED, 'Completed'),
    ]

    label = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=DEFAULT_STATUS, null=False)
    comment = models.TextField(null=True)

    task_user = models.ForeignKey(TaskUser, on_delete=models.CASCADE)


    class Meta:
        unique_together = (('label', 'task_user'))
