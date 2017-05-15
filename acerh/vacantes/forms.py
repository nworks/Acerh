from django import forms
from django.forms import ModelForm, TextInput
from models import Aplicado, Vacante
from django.contrib.auth.models import User

class EntrevistaForm(forms.ModelForm):
	comentario = forms.TextInput(attrs={'class': 'form-control'})
	com_interno = forms.TextInput(attrs={'class': 'form-control'})
	entrevista = forms.TextInput(attrs={'class': 'form-control'})
	class Meta:
		model = Aplicado
		fields = ["comentario","entrevista","com_interno"]
		
	   
class VacantesEdit(forms.ModelForm):
	class Meta:
		model = Vacante
		fields = ["titulo","area","descripcion","requisitos","pregunta"]

