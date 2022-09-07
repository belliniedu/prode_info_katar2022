from django.db import models

from usuarios.models import Usuario
# Create your models here.



class Grupo(models.Model):

	VISIBILIDAD_CHOICES = (
	("P", "Publico"),
	("X","Privado")
)

	nombre=models.CharField(max_length=255)
	creador=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_grupos") # lo borra en cascada o SET_NULL, NOT_NOTHING
	portada=models.ImageField(upload_to="portadas_grupos", null=True, blank=True)
	participantes = models.ManyToManyField(Usuario) #OneToOne

	visibilidad = models.CharField(max_length=1, choices=VISIBILIDAD_CHOICES,default="X")

	class Meta:
		db_table = "grupos"

		

class GrupoUsuarios(models.Model):
	grupo=models.ForeignKey(Grupo, on_delete=models.CASCADE)
	usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)





