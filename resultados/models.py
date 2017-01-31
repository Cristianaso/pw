from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombreEquipo = models.CharField(max_length=20)
	nombreEntrenador = models.CharField(max_length=50)
	puesto = models.IntegerField(default=1)
	puntos = models.IntegerField(default=0)
	def __str__(self):
		return self.nombreEquipo

class Partido(models.Model):
	fecha = models.DateField(auto_now=False,auto_now_add=False)
	hora = models.TimeField(auto_now=False,auto_now_add=False)
	equipoLocal = models.ForeignKey(Equipo)
	nombreLocal = models.CharField(max_length=20)
	nombreVisitante = models.CharField(max_length=20)
	def __unicode__(self):
		return self.nombreLocal+"-"+self.nombreVisitante

class Resultado(models.Model):
	golesLocal = models.CharField(max_length=10,default="?")
	golesVisitante = models.CharField(max_length=10,default="?")
	nombreLocal = models.CharField(max_length=20)
	nombreVisitante = models.CharField(max_length=20)
	partido = models.ForeignKey(Partido)
	def __unicode__(self):
		return self.nombreLocal+"//"+self.nombreVisitante
