from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })



def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })



def book(request, flight_id):
    # For a post request, add a new flight
    if request.method == "POST":

        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))