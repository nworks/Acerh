from django import forms
from models import UserP
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email"]
		

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'Usuario'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))



class UserPr(forms.ModelForm):
		class Meta:
			model = UserP
			fields = ["picture"]


				
class UsuarioForm2(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","password","first_name","last_name","email"]

				
		

