from django.contrib.auth.models import User, Group
from rest_framework import serializers
from vacantes.models import Vacante, Aplicado, Area, Preguntado, Provincia, Compania



class VacanteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
	    #url = serializers.HyperlinkedIdentityField(view_name="acerh:user-detail")
		model = Vacante
		fields = ('titulo','descripcion','creatd_date', 'vigencia','requisitos','pregunta','pregunta1','pregunta2','pregunta3','pregunta4','pregunta5','pregunta6','pregunta7','pregunta8','pais')

