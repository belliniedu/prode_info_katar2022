from django import forms
from  .models import Grupo
from usuarios.models import Usuario

class GrupoForm(forms.ModelForm):

	class Meta:	
		model = Grupo
		fields = ["nombre","participantes"]

	def __init__(self,usuario_id,*args,**kwargs):
		super(GrupoForm, self).__init__(*args,**kwargs)
		self.fields["participantes"].queryset=Usuario.objects.all().exclude(id=usuario_id)