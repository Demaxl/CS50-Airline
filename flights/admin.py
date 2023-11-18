from django.contrib import admin

from .models import Flight, Airport, Passenger
# Register your models here

class FlightAdmin(admin.ModelAdmin):
    """ Configures the interface on the django admin app"""
    list_display = ("id", "origin", "destination", "duration")
 
 
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)


admin.site.register(Flight, FlightAdmin) # Tells django to use the configuration on the admin app
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)
