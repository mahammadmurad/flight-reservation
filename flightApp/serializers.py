from rest_framework import serializers
from flightApp.models import Flights, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
