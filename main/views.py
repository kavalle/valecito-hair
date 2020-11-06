from django.shortcuts import render
from .models import Reserva

from valecitohair import views

def home(request):
    return render(request, "inicio.html")

def reservation(request):
    return render(request, "reservar.html")

def list(request):
    return render(request, "listar.html", { "reservas": Reserva.objects.all() })
