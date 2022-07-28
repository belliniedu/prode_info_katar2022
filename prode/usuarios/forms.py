from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

from dataclasses import fields


class UsuarioRegistroForm(UserCreationForm):
	class Meta:
		model=Usuario
		fields=["first_name","last_name","username","password1","password2"]



