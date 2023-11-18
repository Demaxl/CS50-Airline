from django.urls import path

from . import views


urlpatterns = [
    path("", views.FlightView.as_view(), name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("airport/<str:code>", views.airport, name="airport"),
    path("<int:flight_id>/book", views.book, name="book")
]
