from django.shortcuts import render
from flightApp.models import Flights, Reservation, Passenger
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def find_flights(request):
    flights = Flights.objects.filter(departCity=request.data["departCity"], 
                                    arriveCity=request.data["arriveCity"],
                                    dateOfDeparture=request.data["dateOfDeparture"]).all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def save_reservation(request):
    flight = Flights.objects.get(pk=request.data['flightId'])
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()
    
    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    
    Reservation.save() 
    return Response(status = status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
