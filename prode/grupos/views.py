from django.shortcuts import render

from .models import Grupo

from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin #verifica q el usuario este autenticado
from django.views.generic import ListView

class Crear(LoginRequiredMixin,CreateView):
	model = Grupo
	form_class = GrupoForm
	template_name = "grupos/crear.html"

	def get_success_url(self,**kwargs):
		return reverse('grupos:listar')

		


class Listar(LoginRequiredMixin, ListView):
	template_name = "equipos/listar.html"
	model = Equipo
	context_object_name = "equipos"


class Actualizar(LoginRequiredMixin, UpdateView):
	model = Equipo
	form_class = EquipoForm
	template_name = "equipos/actualizar.html"

	def get_success_url(self,**kwargs):
		return reverse('equipos:actualizar')







