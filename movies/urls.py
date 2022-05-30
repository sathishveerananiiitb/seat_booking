from django.urls import path
from .views import index

app_name = 'seat_booking'

urlpatterns = [
    path('',index,name="home")
]
