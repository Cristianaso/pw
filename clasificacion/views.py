from django.shortcuts import render
from django.http import HttpResponse
from clasificacion.models import Equipo

# Create your views here.

def vistaClasificacion(request):
	posiciones = Equipo.objects.all()
	context = {'posiciones': posiciones}
	
	return render(request, "clasificacion.html", context)
