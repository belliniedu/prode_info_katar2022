from django.db import models

class Equipo(models.Model):
	nombre = models.CharField(max_length=255) # crea table del tipo varchar
	logo = models.ImageField(upload_to="logo_equipos", null=True, blank=True)
	def __str__(self):
		return self.nombre