from django.db import models

# Create your models here.
# events/models.py

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_time = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    
    class Meta:
        app_label = 'events'
    
    def __str__(self):
        return self.event_name
