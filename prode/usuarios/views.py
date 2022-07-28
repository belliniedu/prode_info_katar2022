from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UsuarioRegistroForm
from .models import Usuario
from django.urls import reverse

class Registro(CreateView):
	model = Usuario
	form_class = UsuarioRegistroForm
	template_name = "usuarios/registro.html"

	def get_success_url(self,**kwargs):
		return reverse('home')









# Create your views here.
