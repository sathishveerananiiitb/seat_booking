from django.shortcuts import render
from .models import Movie, Payment, PaymentIntent, Seat
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings

import json
import requests;

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

@csrf_exempt
def makePayement(request):
    data=json.loads(request.body)
    seat_numbers=list(map(lambda seat: seat+1,data["seat_list"]))
    movie_title=data["movie_title"]

    cost=Movie.objects.get(title=movie_title).price

    header={
        "Authorization":f"Bearer {settings.PAYSTACK_SECRET}",
        "Content-Type":"application/json"
    }

    data={
        "name":"Payment of Movie Ticket",
        "amount":int(cost*len(seat_numbers))*100,
        "description":f"Payment for {len(seat_numbers)} ticket of {movie_title}",
        "collect_phone":True,
        "redirect_url":f"{settings.HOST_URL}/payment-confirm/"
    }

    response=requests.post('https://api.paystack.co/page',
                            json=data,headers=header)

    if response.status_code ==200:
        response_data=response.json()
        slug=response_data["data"]["slug"]
        redirect_url=f"https://paystack.com/pay/{slug}"

        PaymentIntent.objects.create(referrer=redirect_url,
                                    movie_title=movie_title,
                                    seat_number=seat_numbers)
        
        return JsonResponse({
            "payment_url":redirect_url
        })

    return JsonResponse({
        "error":"sorry service is not available"
    })
