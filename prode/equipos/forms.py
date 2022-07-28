from dataclasses import fields
from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
	nombre=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"})) # widget es para darle forma
	#cantidad_jugadores=forms.IntegerField()
	class Meta:
		model = Equipo
		fields = ["nombre"] # elejir que campos se quieren cambiar o ingresar

	def clean_nombre(self):		
		nombre = self.cleaned_data["nombre"] #se usa para validar campos
		if nombre[0] != "A":
			raise forms.ValidationError("El nombre debe iniciar con A") #genera una excepcion osea retorna
		return nombre





