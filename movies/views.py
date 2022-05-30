from django.shortcuts import render
from .models import Movie, Payment, PaymentIntent, Seat
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json

# Create your views here.
def index(request):
    movies=Movie.objects.all()
    return render(request,"index.html",{
        "movies":movies
    })

@csrf_exempt
def occupiedSeats(request):
    data=json.loads(request.body)

    movie=Movie.objects.get(title=data["movie_title"])
    occupied=movie.booked_seats.all()
    occupied_seat=list(map(lambda seat : seat.seat_no - 1,occupied))

    return JsonResponse({
        "occupied_seats":occupied_seat,
        "movie":str(movie)
    })
