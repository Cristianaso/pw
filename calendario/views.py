from django.shortcuts import render
from django.http import HttpResponse
from calendario.models import Partido

# Create your views here.

def vistaCalendario(request):
	jornadas = Partido.objects.all()
	context = {'jornadas': jornadas}
	
	return render(request, "calendario.html", context)
