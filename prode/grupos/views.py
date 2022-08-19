from django.shortcuts import render

from .models import Grupo
from .forms import GrupoForm
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin #verifica q el usuario este autenticado
from django.views.generic import ListView

"""
class Crear(LoginRequiredMixin,CreateView):
	model = Grupo
	form_class = GrupoForm
	template_name = "grupos/crear.html"

	def get_success_url(self,**kwargs):
		return reverse('grupos:listar')
"""
		

class Listar(LoginRequiredMixin, ListView):
	template_name = "grupos/listar.html"
	model = Grupo
	context_object_name = "grupos"
	paginate_by=3

	def get_context_data(self, **kwargs): # Es para pasarle un contexto
		context=super().get_context_data(**kwargs)
		#context["dato"] = "Un dato"
		print(self.request.user.mis_grupos.all()) #Es otra forma de hacer el filtrado de los grupos que hizo el user
		return context

	def get_queryset(self):
		return Grupo.objects.filter(creador=self.request.user)


"""
class Actualizar(LoginRequiredMixin, UpdateView):
	model = Equipo
	form_class = EquipoForm
	template_name = "equipos/actualizar.html"

	def get_success_url(self,**kwargs):
		return reverse('equipos:actualizar')
"""

class Crear(LoginRequiredMixin, CreateView):
	model= Grupo
	template_name = "grupos/crear.html"
	form_class= GrupoForm

	def form_valid(self, form):
		f= form.save(commit=False) # le digo que no lo guarde todavia
		f.creador_id=self.request.user.id #le asigno manualmente el campo
		return super(Crear, self).form_valid(form)

	def get_success_url(self, **kwargs):
		return reverse('grupos:listar')

	def get_form_kwargs(self):
		kwargs=super(Crear, self).get_form_kwargs()
		kwargs["usuario_id"]=self.request.user.id
		return kwargs



