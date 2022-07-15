from django.shortcuts import render
from re import template
def inicio(request):
	template_name="inicio.html"
	usuario={
		"nombre":"Lucas",
		"apellido":"Bulo"
	}
	ctx={
		"user_dict": usuario
	}
	return render(request, template_name,ctx)