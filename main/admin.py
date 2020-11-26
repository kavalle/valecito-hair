from django.contrib import admin
from .models import Reserva, Usuario

class ReservaAdmin(admin.ModelAdmin):
    # readonly_fields=("hora")
    list_display=["nombre_completo", "correo", "telefono", "hora"]
    search_fields=["nombre_completo"]
    list_filter=["nombre_completo","telefono"]

class UsuarioAdmin(admin.ModelAdmin): 
    list_display=["usuario"]
    search_fields=["usuario"]
    list_filter=["usuario"]


# Register your models here.
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Usuario, UsuarioAdmin)