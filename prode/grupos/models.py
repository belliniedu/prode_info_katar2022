from django.db import models

from usuarios.models import Usuario
# Create your models here.

class Grupo(models.Model):
	nombre=models.CharField(max_length=255)
	creador=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_grupos") # lo borra en cascada o SET_NULL, NOT_NOTHING

	participantes = models.ManyToManyField(Usuario) #OneToOne

	class Meta:
		db_table = "grupos"

		
"""
class GrupoUsuarios(models.Model):
	grupo=model.ForeignKey(Usuario, on_delete=models.CASCADE)
	usuario=model.ForeignKey(Usuario, on_delete=models.CASCADE)
"""




