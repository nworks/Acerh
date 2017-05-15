from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models

def upload_location(instancia, filename):
	return "CV/%s/%s" %(instancia.id, filename)


# Create your models here.
class UserP(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='userpic/', blank=True)
	file = models.FileField(upload_to=upload_location, blank=True)
	localidad = models.CharField(max_length=50, blank=True)
	estudio = models.CharField(max_length=100, blank=True)
	edad = models.CharField(max_length=50, blank=True)
	experiencia = models.CharField(max_length=50, blank=True)
	idioma = models.TextField(blank=True)
	ar_exp = models.CharField(max_length=50, blank=True)
	ar_int = models.CharField(max_length=50, blank=True)
	carrera = models.CharField(max_length=50, blank=True)
	sexo = models.CharField(max_length=50, blank=True)
	cedula = models.CharField(max_length=20          , blank=True)
	salario = models.CharField(max_length=100, blank=True)
	nacionalidad = models.CharField(max_length=50, blank=True)
	universidad = models.CharField(max_length=50, blank=True)
	licencia = models.CharField(max_length=50, blank=True)
	cat_licen = models.CharField(max_length=25, blank=True)
	pais_apli = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.user.username

class UserPC(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='companypic/', blank=True)
	company = models. BooleanField()
	descripcion = models.TextField()
	
	def __str__(self):
		return self.user.username

class notify(models.Model):
	user = models.OneToOneField(User)
	message = models.TextField()
	company = models.OneToOneField(User, related_name='company')
	
	def __str__(self):
		return self.user.username        



