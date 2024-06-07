from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_events'
    )
    name = models.CharField(max_length=128)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    attendees = models.ManyToManyField(
        User, related_name='events', null=True, blank=True
    )

    def __str__(self):
        return self.name
