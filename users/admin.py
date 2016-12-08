from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from users.models import UserP
# Register your models here.
admin.site.register(UserP)
