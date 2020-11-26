from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.home, name='index'),
    path('reservar', views.reservation, name='reservar'),
    path('listar-reservas', views.list, name='listar'),
    path('validar-reserva', views.valid, name='validar'),
    path('iniciar-sesion', views.login, name="login"),
    path('cerrar-sesion', views.logout, name="logout"),
    path('validar-login', views.valid_login, name="validar-login"),
    path('api/reservas', views.lastReserva, name="ultima")
]
