from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models



def upload_location(instancia, filename):
	return "EN/%s/%s" %(instancia.id, filename)
# Create your models here.
class Area(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.TextField(blank=True)
	
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
	pregunta = models.TextField(blank=True)
	pregunta1 = models.TextField(blank=True)
	pregunta2 = models.TextField(blank=True)
	pregunta3 = models.TextField(blank=True)
	pregunta4 = models.TextField(blank=True)
	pregunta5 = models.TextField(blank=True)
	pregunta6 = models.TextField(blank=True)
	pregunta7 = models.TextField(blank=True)
	pregunta8 = models.TextField(blank=True)
	
	class Meta:
		ordering = ["-creatd_date"]

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
	com_interno = models.TextField()
	estatus2 = models.CharField(max_length=15)
	entrevista = models.FileField(upload_to=upload_location, blank=True)
	respuesta = models.TextField(blank=True)
	respuesta2 = models.TextField(blank=True)
	respuesta3 = models.TextField(blank=True)
	respuesta4 = models.TextField(blank=True)
	respuesta5 = models.TextField(blank=True)
	respuesta6 = models.TextField(blank=True)
	respuesta7 = models.TextField(blank=True)
	respuesta8 = models.TextField(blank=True)
	com_interno = models.TextField()

	
	def __str__(self):
		return str(self.id)



class Provincia(models.Model):
	provincia = models.CharField(max_length=60)
	area = models.CharField(max_length=60,blank=True)

	
	def __str__(self):
		return self.provincia


class Preguntado(models.Model):
	titulo = models.CharField(max_length=60)
	pregunta = models.TextField()
	emisor = models.ForeignKey(User)
	destinatario = models.ForeignKey(User,related_name='destinatario')
	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	estatus = models.CharField(max_length=60)



	
	def __str__(self):
		return self.titulo

