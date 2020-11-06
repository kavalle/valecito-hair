from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva

from valecitohair import views

def home(request):
    return render(request, "inicio.html")

def reservation(request):
    return render(request, "reservar.html", { "exito": False })

def list(request):
    return render(request, "listar.html", { "reservas": Reserva.objects.all() })

def valid(request):
    print (request.method)
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