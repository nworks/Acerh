from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models



def upload_location(instancia, filename):
	return "CV/%s/%s" %(instancia.id, filename)
# Create your models here.
class Area(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField()
	
	def __str__(self):
		return self.titulo

class Vacantes(models.Model):
	titulo = models.CharField(max_length=100)
	area = models.ForeignKey(Area)
	descripcion = models.TextField()
	picturep = models.ImageField(upload_to='vacantes/', blank=True)
	compania = models.ForeignKey(User)
	creatd_date = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __str__(self):
		return str(self.id)

class Vacante(models.Model):
	titulo = models.CharField(max_length=100)
	area = models.ForeignKey(Area)
	descripcion = models.TextField()
	picturep = models.ImageField(upload_to='vacantes/', blank=True)
	compania = models.ForeignKey(User)
	creatd_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	vigencia = models.CharField(max_length=100)
	requisitos = models.TextField()
	pregunta = models.CharField(max_length=100)

	def __str__(self):
		return str(self.id )

class Estatus(models.Model):
	titulo = models.CharField(max_length=20)
	descripcion = models.TextField()
	
	def __str__(self):
		return self.titulo

class Aplicado(models.Model):
	usuario = models.ForeignKey(User)
	aplico = models.ForeignKey(Vacante)
	estatus = models.ForeignKey(Estatus)
	comentario = models.TextField()
	estatus2 = models.CharField(max_length=15)
	entrevista = models.FileField(upload_to=upload_location, blank=True)

	
	def __str__(self):
		return str(self.id)


