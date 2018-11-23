from django.db import models

class Usuario(models.Model):
	
	nombre_usuario = models.CharField(max_length=30)
	apellido_usuario = models.CharField(max_length=30)
	rut_usuario = models.CharField(max_length=30)
	comuna_usuaro = models.CharField(max_length=30)
	lugar_trabajo = models.CharField(max_length=30)
	def __str__(self):
		return self.nombre_usuario
# Create your models here.
