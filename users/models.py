from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models

# Create your models here.
class UserP(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='userpic/', blank=True)
	
	def __str__(self):
		return self.user.username