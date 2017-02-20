from django import forms
from django.forms import ModelForm, TextInput
from models import Aplicado
from django.contrib.auth.models import User

class EntrevistaForm(forms.ModelForm):
    comentario = forms.TextInput(attrs={'class': 'form-control'})
    entrevista = forms.TextInput(attrs={'class': 'form-control'})
    class Meta:
		model = Aplicado
		fields = ["comentario","entrevista"]
        
       
