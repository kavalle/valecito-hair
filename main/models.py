from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre_completo= models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=10)
    servicio = models.CharField(max_length=50)
    hora = models.TimeField()