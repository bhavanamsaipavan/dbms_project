from django.db import models
from django.contrib.auth.models import User

# events/models.py
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    host_details = models.TextField(default='Tell about yourself')
    event_time = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    event_fee = models.IntegerField(default=0)
    event_image = models.ImageField(upload_to='event_images/', default='event_images/default_image.webp')  # New field for the event image

    class Meta:
        app_label = 'events'


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} registered for {self.event.event_name}"

    def __str__(self):
        return self.event_name
