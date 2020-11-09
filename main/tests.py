from django.test import TestCase
from .models import Reserva

class BasicTest(TestCase):
  def test_fields(self):
      nueva_reserva = Reserva(
        nombre_completo = 'Sady Bachmann',
        correo = 'sa.bachmann@alumnos.duoc.cl',
        telefono = '981648865',
        servicio = 'Corte de pelo',
        hora = '00:00'
      )
      nueva_reserva.save()
      record = Reserva.objects.get(id=1)
      self.assertEqual(record)

  def test_error(self):
      nueva_reserva = Reserva(
        nombre_completo = 'Sady Bachmann',
        correo = 'sa.bachmann@alumnos.duoc.cl',
        telefono = '',
        servicio = 'Corte de pelo',
        hora = '00:00'
      )
      nueva_reserva.save()
      record = Reserva.objects.get(id=1)
      self.assertEqual(record)