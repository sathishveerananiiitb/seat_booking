from django.urls import path
from .views import index,occupiedSeats

app_name = 'seat_booking'

urlpatterns = [
    path('',index,name="home"),
    path('occupied/',occupiedSeats,name="occupied_seat"),
]
