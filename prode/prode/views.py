from django.shortcuts import render
from django.views.generic import TemplateView
from re import template
from equipos.models import Equipo
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from core.mixins import superuser_required

#@superuser_required
def inicio(request):
	template_name="inicio.html"	

	#equipos = Equipo.objects.filter(nombre="Argentina") #query --> consulta mediante el orm
	"""print("***********")
	print(equipos.query)"""

	"""Equipo.objects.create(
		nombre="Alemania"
		) """
	ctx={}
	return render(request, template_name,ctx)



"""
def login(request):
	print("----------")
	print(request.POST)
	if request.method == "POST":
		nombre_usuario=request.POST.get("username",None)
		contrasenia=request.POST.get("password",None)
		Equipo.objects.create(
			nombre=nombre_usuario
			)

	return render(request, "login.html",{})
"""



"""vista basada en funcion
"""
@login_required# decorador
def mis_grupos(request):
	return render(request, "mis_grupos.html",{})
"""
class MisGrupos(TemplateView):
	template_name = "mis_grupos.html"
"""

class LoginView(TemplateView):
	template_name = "login.html"
