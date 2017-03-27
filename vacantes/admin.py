from django.contrib import admin
from vacantes.models import Vacantes,Area,Estatus,Aplicado, Vacante, Preguntado, Provincia
# Register your models here.
admin.site.register(Vacante)
admin.site.register(Area)
admin.site.register(Estatus)
admin.site.register(Aplicado)
admin.site.register(Preguntado)
admin.site.register(Provincia)