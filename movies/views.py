from django.shortcuts import render
from .models import Movie, Payment, PaymentIntent, Seat

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    return render(request,"index.html",{
        "movies":movies
    })