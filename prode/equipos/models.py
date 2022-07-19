from django.db import models

class Equipo(models.Model):
	nombre = models.CharField(max_length=255) # crea table del tipo varchar

	def __str__(self):
		return self.nombre