from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # Creates a foreignkey that references the primary key of the airport model
    # on_delete=models.CASCADE means when the primary key that is being referenced is deleted, 
    # the corresponding row should also be deleted.
    # related_name is used to access the relationship in the reverse order i.e,
    # the airport model will be able to access all the flights that have the airport as origin or destination

    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
    def is_valid_flight(self):
        return self.origin != self.destination or self.duration >= 0


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    """ 
    ManyToManyField is used to represent the logic that a flight can have multiple passengers
    and a passenger can be on multiple flights. Think of a table with columns "flight_id" and "passenger_id"
    this represents something like that. blank allows the possibility that a passenger has no flights.
    related_name same as before

    """
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
    