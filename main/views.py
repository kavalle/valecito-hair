from django.shortcuts import render

from valecitohair import views

def home(request):
    return render(request, "index.html")
