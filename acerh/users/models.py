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
	localidad = models.CharField(max_length=100, blank=True)
	estudio = models.CharField(max_length=100, blank=True)
	edad = models.CharField(max_length=100, blank=True)
	experiencia = models.TextField(blank=True)
	idioma = models.TextField(blank=True)
	ar_exp = models.TextField(blank=True)
	ar_int = models.TextField(blank=True)
	carrera = models.CharField(max_length=100, blank=True)
	sexo = models.CharField(max_length=100, blank=True)
	cedula = models.CharField(max_length=100, blank=True)
	salario = models.CharField(max_length=100, blank=True)
	nacionalidad = models.CharField(max_length=100, blank=True)
	universidad = models.CharField(max_length=100, blank=True)
	licencia = models.CharField(max_length=100, blank=True)
	cat_licen = models.CharField(max_length=100, blank=True)
	pais_apli = models.CharField(max_length=100, blank=True)
	telefono = models.CharField(max_length=100, blank=True)
	fec_nac = models.CharField(max_length=20, blank=True)
	edad2 = models.CharField(max_length=10, blank=True)

	def __unicode__(self):
		return self.user.username

class UserPC(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='companypic/', blank=True)
	company = models. BooleanField()
	descripcion = models.TextField()
	
	def __unicode__(self):
		return self.user.username

class notify(models.Model):
	user = models.OneToOneField(User)
	message = models.TextField()
	company = models.OneToOneField(User, related_name='company')
	
	def __unicode__(self):
		return self.user.username        



