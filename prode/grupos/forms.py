from django import forms
from  .models import Grupo
from usuarios.models import Usuario

class GrupoForm(forms.ModelsForm):

	class Meta:	
		model = Grupo
		field = ["nombre","participantes"]

	def __init__(self,usuario_id,*args,**kwargs):
		super()