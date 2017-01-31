from django.shortcuts import render
from django.http import HttpResponse
from equipos.models import Equipo

# Create your views here.

def vistaEquipo(request):
	listaEquipos = Equipo.objects.all()
	context = {'listaEquipos': listaEquipos}
	
	return render(request, "equipos.html", context)
