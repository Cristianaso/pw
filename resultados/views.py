from django.shortcuts import render
from django.http import HttpResponse
from resultados.models import Resultado

# Create your views here.

def vistaResultados(request):
	resultados = Resultado.objects.all()
	context = {'resultados': resultados}
	
	return render(request, "resultados.html", context)
