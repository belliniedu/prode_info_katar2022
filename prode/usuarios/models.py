from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	telefono=models.CharField(max_length=255, null=True, blank=True)

	def __srt__(self):
		return self.first_name + " " + self.last_name





# Create your models here.
