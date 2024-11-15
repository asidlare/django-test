from django.db import models
from core.models.utils import TimeStampedModel


class TaskUser(TimeStampedModel):
    email = models.EmailField(unique=True, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
