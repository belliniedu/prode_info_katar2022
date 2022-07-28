from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Equipo
from .forms import EquipoForm
from django.contrib.auth.mixins import LoginRequiredMixin #verifica q el usuario este autenticado
from django.views.generic import ListView

class Crear(LoginRequiredMixin,CreateView):
	model = Equipo
	form_class = EquipoForm
	template_name = "equipos/crear.html"

	def get_success_url(self,**kwargs):
		return reverse('equipos:listar')

class Listar(LoginRequiredMixin, ListView):
	template_name = "equipos/listar.html"
	model = Equipo
	context_object_name = "equipos"


