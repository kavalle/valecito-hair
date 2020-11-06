from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    # readonly_fields=("hora")
    list_display=["nombre_completo", "correo", "telefono", "hora"]
    search_fields=["nombre_completo"]
    list_filter=["nombre_completo","telefono"]


# Register your models here.
admin.site.register(Reserva, ReservaAdmin)