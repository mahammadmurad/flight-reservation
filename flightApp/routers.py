from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('flight', views.FlightViewSet)
router.register('passenger', views.PassengerViewSet)
router.register('reservation', views.ReservationViewSet)