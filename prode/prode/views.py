from django.shortcuts import render
from django.views.generic import TemplateView
from re import template
from equipos.models import Equipo

def inicio(request):
	template_name="inicio.html"	

	equipos = Equipo.objects.filter(nombre="Argentina") #query --> consulta mediante el orm
	"""print("***********")
	print(equipos.query)"""

	"""Equipo.objects.create(
		nombre="Alemania"
		) """

	ctx={
		'equipos': equipos,
		'nombre': "Edu"
	}
	return render(request, template_name,ctx)


def login(request):
	return render(request, "login.html",{})

"""vista basada en funcion
def mis_grupos(request):
	return render(request, "mis_grupos.html",{})
"""
class MisGrupos(TemplateView):
	template_name = "mis_grupos.html"



	