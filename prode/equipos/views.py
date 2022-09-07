from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Equipo
from .forms import EquipoForm
from django.contrib.auth.mixins import LoginRequiredMixin #verifica q el usuario este autenticado
from django.views.generic import ListView
from core.mixins import SuperUserRequiredMixin
from core.mixins import AdminUserRequiredMixin

class Crear(LoginRequiredMixin, AdminUserRequiredMixin, CreateView):
	model = Equipo
	form_class = EquipoForm
	template_name = "equipos/crear.html"

	def get_success_url(self,**kwargs):
		return reverse('equipos:listar')

class Listar(LoginRequiredMixin, SuperUserRequiredMixin, ListView):
	template_name = "equipos/listar.html"
	model = Equipo
	context_object_name = "equipos"
	paginate_by=4
	def get_queryset(self):
		return Equipo.objects.all().order_by("id")



class Actualizar(LoginRequiredMixin, UpdateView):
	model = Equipo
	form_class = EquipoForm
	template_name = "equipos/actualizar.html"

	def get_success_url(self,**kwargs):
		return reverse('equipos:listar')
