# contact/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)  # New field
    query = models.TextField()

    def __str__(self):
        return self.name
