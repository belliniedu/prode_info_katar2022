from django.shortcuts import render
from re import template
from equipos.models import Equipo

def inicio(request):
	template_name="inicio.html"	

	equipos = Equipo.objects.all()
	print(equipos)

	ctx={
		'equipos': equipos,
		'nombre': "Edu"
	}
	return render(request, template_name,ctx)


def login(request):
	return render(request, "login.html",{})