from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView

from django.urls import reverse


from .models import Airport, Flight, Passenger

# Create your views here.
class FlightView(ListView):
    model = Flight
    context_object_name = "all_flights"
    template_name = "index.html"


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)


    return render(request, "flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        # Returns a list of passengers who are not on the flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def airport(request, code):
    try:
        port = Airport.objects.get(code=code.upper())

        return render(request, "airport.html", {
            "port": port,
            "arrivals": port.arrivals.all(),
            "departures": port.departures.all()
        })
    except:
        return HttpResponse("<h1>The requested airport does not exist</h1>")

def book(request, flight_id):
    if request.method == "POST":

        # Gets the flight to book
        flight = Flight.objects.get(pk=flight_id)
        # Gets the passenger posted
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))

        # # Adds a new flight to the passengers set of flights
        passenger.flights.add(flight)

        # Redirects to the flight route and pass the flight id as argument
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
