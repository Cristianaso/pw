from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombreEquipo = models.CharField(max_length=20)
	nombreEntrenador = models.CharField(max_length=50)
	puesto = models.IntegerField(default=1)
	puntos = models.IntegerField(default=0)
	def __str__(self):
		return self.nombreEquipo
