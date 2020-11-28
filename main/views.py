from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva
from django.core import serializers
from django.contrib.auth import authenticate

from valecitohair import views

#rest_framework

from rest_framework import viewsets
from .serializers import ReservasSerializer


# consumo api

from urllib.request import urlopen
import json


def home(request):
    return render(request, "inicio.html", { "logeado": request.user.is_authenticated})

def reservation(request):
    return render(request, "reservar.html", { "exito": False })

def list(request):
    if request.user.is_authenticated:

        # url="https://api.gael.cl/general/public/monedas/UTM"
        # datos = urlopen(url).read()
        # moneda = json.loads(datos)
        # valor = moneda["Valor"]

        valor = 11111

        return render(request, "listar.html", { "reservas": Reserva.objects.all(), "valor_uf": valor })
    else:
        return redirect('/accounts/login/')

def valid(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")
        correo = request.POST.get("correo")
        servicio = request.POST.get("servicio")
        hora = request.POST.get("hora")

        nueva_reserva = Reserva(
            nombre_completo = nombre,
            correo = correo,
            telefono = telefono,
            servicio = servicio,
            hora = hora
        )
        nueva_reserva.save()
        return render(request, "reservar.html", { "exito": True })
    return HttpResponse("Error")

def lastReserva(request):

    reservas = Reserva.objects.all()
    print(reservas)
    return HttpResponse(
        serializers.serialize("json", reservas),
        content_type="application/json"
    )

class AppViewSet(viewsets.ModelViewSet):
    queryset= Reserva.objects.all()
    serializer_class=ReservasSerializer