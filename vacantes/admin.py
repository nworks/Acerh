from django.contrib import admin
from vacantes.models import Vacantes,Area,Estatus,Aplicado
# Register your models here.
admin.site.register(Vacantes)
admin.site.register(Area)
admin.site.register(Estatus)
admin.site.register(Aplicado)