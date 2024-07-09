from django.db import models

class Flights(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departCity = models.CharField(max_length=20)
    arriveCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Reservation(models.Model):
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
