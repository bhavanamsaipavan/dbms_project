from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_time = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    event_image = models.ImageField(upload_to='event_images/', default='default_image.jpg')  # New field for the event image

    class Meta:
        app_label = 'events'

    def __str__(self):
        return self.event_name
