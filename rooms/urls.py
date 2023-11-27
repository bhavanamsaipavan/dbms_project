
# rooms/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Accomodation, name='room_list'),
    path('room/<uuid:room_id>/', views.hotel_detail, name='room_detail'),
    # path('room/<int:room_id>/register/', views.register_for_room, name='register_for_room'),
    path('my_registered_rooms/', views.user_registered_rooms, name='my_registered_rooms'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)