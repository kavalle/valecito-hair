from django.urls import path, include
from . import views

from rest_framework import routers
from .views import AppViewSet

router = routers.DefaultRouter()
router.register('reservas', AppViewSet)


app_name='main'

urlpatterns = [
    path('', views.home, name='index'),
    path('reservar', views.reservation, name='reservar'),
    path('validar-reserva', views.valid, name='validar'),
    path('api/',include(router.urls)),
]
