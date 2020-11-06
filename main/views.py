from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva

from valecitohair import views

def home(request):
    return render(request, "inicio.html")

def reservation(request):
    return render(request, "reservar.html")

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

        return render(request, "reservar.html", { "exito": TRUE })
    return HttpResponse("NO")