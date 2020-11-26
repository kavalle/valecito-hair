from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva, Usuario

from valecitohair import views

def home(request):
    return render(request, "inicio.html")

def reservation(request):
    return render(request, "reservar.html", { "exito": False })

def list(request):
    sess = request.session.get('usuario')
    if sess == None:
        return redirect('/iniciar-sesion')
    return render(request, "listar.html", { "reservas": Reserva.objects.all() })


def logout(request):
    del request.session['usuario']
    return redirect("/")

def login(request):
    return render(request, "login.html")

def valid_login(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        contrasena = request.POST.get("contrasena")

        try:
            obj = Usuario.objects.get(usuario=usuario, contrasena=contrasena)
            request.session['usuario'] = obj.usuario
            return redirect("/listar-reservas")
        except Usuario.DoesNotExist:
            return render(request, "login.html", { "fallido": True }) 


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