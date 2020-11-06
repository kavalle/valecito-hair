from django.shortcuts import render

from valecitohair import views

def home(request):
    return render(request, "inicio.html")

def reservation(request):
    return render(request, "reservar.html")
