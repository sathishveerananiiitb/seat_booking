from django.urls import path
from .views import index,occupiedSeats,makePayement,getDetails

app_name = 'seat_booking'

urlpatterns = [
    path('',index,name="home"),
    path('occupied/',occupiedSeats,name="occupied_seat"),
    path('payment/',makePayement,name="payment"),
    path('user_details/',getDetails,name="user_details")
]
