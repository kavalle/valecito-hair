from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva
from django.core import serializers
from django.contrib.auth import authenticate

from valecitohair import views

def home(request):
    return render(request, "inicio.html", { "logeado": request.user.is_authenticated})

def reservation(request):
    return render(request, "reservar.html", { "exito": False })

def list(request):
    if request.user.is_authenticated:
        return render(request, "listar.html", { "reservas": Reserva.objects.all() })
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