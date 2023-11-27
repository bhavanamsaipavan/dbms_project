# from django.db import models
# from django.contrib.auth.models import User

# # rooms/models.py
# class room(models.Model):
#     room_name = models.CharField(max_length=255)
#     room_description = models.TextField()
#     host_details = models.TextField(default='Tell about yourself')
#     room_time = models.DateTimeField()
#     room_location = models.CharField(max_length=255)
#     room_fee = models.IntegerField(default=0)
#     room_image = models.ImageField(upload_to='room_images/', default='room_images/default_image.webp')  # New field for the room image

#     class Meta:
#         app_label = 'rooms'


# class Registration2(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(room, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('user', 'room')

#     def __str__(self):
#         return f"{self.user.username} registered for {self.room.room_name}"

#     def __str__(self):
#         return self.room_name

# from statistics import mode
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4   , editable=False , primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Hotel(BaseModel):
    hotel_name= models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.CharField(max_length=300)
    room_count = models.IntegerField(default=10)
    room_image = models.ImageField(upload_to='room_images/', default='room_images/default_image.webp')  # New field for the room image
    available_rooms = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name


class HotelBooking(BaseModel):
    hotel= models.ForeignKey(Hotel  , related_name="hotel_bookings" , on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))
    
    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("End date must be after the start date")

    def save(self, *args, **kwargs):
        self.clean()  # Validate dates before saving
        super().save(*args, **kwargs)
        self.hotel.available_rooms -= 1
        self.hotel.save()