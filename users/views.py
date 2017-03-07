from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse
from users.forms import LoginForm ,UserP, UsuarioForm2, UserPr,PasswordResetRequestForm,SetPasswordForm, UsuarioForm
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from vacantes.models import Vacante, Aplicado
from django.db import models
from users.models import UserPC, UserP
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from smtplib import SMTPRecipientsRefused
from django.core.mail import EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from django.template import Library
from django.template.defaulttags import cycle as cycle_original
from django.core.urlresolvers import reverse

# Create your views here.

@csrf_protect
def LoginRequest(request):
	message = "Credenciales invalidas o No registradas"
	# Si el usuario ya ha iniciado sesion anteriormente.
	if request.user.is_authenticated():
		return HttpResponseRedirect('/vacantes')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		# Si el formulario es valido, iniciar la sesion y redireccionar
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			usuario = authenticate(username=username,password=password)
			if usuario is not None:
				login(request,usuario)
				if request.user.is_staff:

					return HttpResponseRedirect('/compania')
				else:
					return HttpResponseRedirect('/vacantes')
			# De lo contrario devolver al Login
			else:
				render(request, "login2.html", {'form':form})
				return render(request, "login2.html", {'form':form, 'message':message})
		# Si el formulario es invalido devolver al login
		else:
			
			return render(request, "login2.html", {'form':form } )
	else:
		form = LoginForm()
		context = {'form':form}
		return render(request, "login2.html", {'form':form})


def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/login')


def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UsuarioForm2(data=request.POST)
		profile_form = UserPr(data=request.FILES)
		data2 = request.POST['username']
		if User.objects.filter(username=data2).exists():
			message = "Este Username ya se encuentra en uso, intente otro"
			return render (request,'registerbeta.html',{'user_form':user_form, 'profile_form': profile_form, 'message':message})


		data = request.POST['email']
		if User.objects.filter(email=data).exists():
			message = "Este correo electronico fue regustrado"
			return render (request,'registerbeta.html',{'user_form':user_form, 'profile_form': profile_form, 'message':message})
		 
		else:
			if user_form.is_valid() and profile_form.is_valid():
				user = user_form.save()
				user.set_password(user.password)
				user.save()

			

				if 'picture' in request.FILES:
					profile = profile_form.save(commit=False)
					profile.user = user
					profile.cedula = request.POST['cedula']
					profile.sexo = request.POST['sexo']
					profile.idioma = request.POST.getlist('idioma')
					profile.carrera = request.POST['carrera']
					profile.ar_int = request.POST['ar_int']
					profile.salario = request.POST['salario']
					profile.telefono = request.POST['telefono']

					profile.picture = request.FILES['picture']
					profile.file = request.FILES['file']
					profile.localidad = request.POST['localidad']
					profile.estudio = request.POST['estudio']
					profile.edad = request.POST['edad']
					profile.experiencia = request.POST['experiencia']
					profile.nacionalidad = request.POST['nacionalidad']
				
					 
					profile.save()
					registered = True
					username = user_form.cleaned_data['username']
					password = user_form.cleaned_data['password']
					usuario = authenticate(username=username,password=password)
					login(request,usuario)
					return HttpResponseRedirect('/vacantes')
				else:
					print user_form.errors, profile_form.errors
	
					profile = profile_form.save(commit=False)
					profile.user = user
					profile.save()
					registered = True
					username = user_form.cleaned_data['username']
					password = user_form.cleaned_data['password']
					profile.file = request.FILES['file']
					
					profile.cedula = request.POST['cedula']
					profile.sexo = request.POST['sexo']
					profile.idioma = request.POST.getlist('idioma')
					profile.carrera = request.POST['carrera']
					profile.ar_int = request.POST['ar_int']
					profile.salario = request.POST['salario']
					profile.telefono = request.POST['telefono']

					profile.localidad = request.POST['localidad']
					profile.estudio = request.POST['estudio']
					profile.edad = request.POST['edad']
					profile.experiencia = request.POST['experiencia']
					profile.nacionalidad = request.POST['nacionalidad']
				
					profile.save()
					usuario = authenticate(username=username,password=password)
					login(request,usuario)
					return HttpResponseRedirect('/vacantes')
	else:
		user_form = UsuarioForm2()
		profile_form = UserPr()	
		return render (request,'registerbeta.html',{'user_form':user_form, 'profile_form': profile_form})


		



def userdetail(request):
	userinfo = User.objects.get(id=request.user.id)
	aplicado = Aplicado.objects.filter(usuario=request.user)
	cantidad = aplicado.count()
	userdetalle = UserP.objects.filter(user=request.user)
	context = { "aplicado":aplicado, "aplicados":aplicado.all() ,"cantidad":cantidad,"userdetalle":userdetalle,"userdetalles":userdetalle.all()}
	context2 = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UsuarioForm(data=request.POST)
		profile_form = UserPr(data=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			
			user = user_form.save()
			user.username = request.user.username
			user.save()
			profile = profile_form.save(commit=False)
			profile.file = request.FILES['file']
			profile.localidad = request.POST['localidad']
			profile.estudio = request.POST['estudio']
			profile.edad = request.POST['edad']
			profile.experiencia = request.POST['experiencia']
			
			profile.user = user
			profile.save()
			registered = True
	return render(request, 'profile.html', context)





def email(request):
	email = EmailMessage()
	email.subject = "Hola mensaje de prueba desde el servidor de acerh"
	email.body = "Coneccion totalmente lograda, prueba test #2"
	email.to = [ "nworks16@gmail.com"]
	email.send()



from collections import OrderedDict

from django import forms
from django.core.mail import EmailMultiAlternatives
from django.forms.utils import flatatt
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from django.views.generic import *

from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q

class ResetPasswordRequestView(FormView):
	template_name = "test_template.html"    #code for template is given below the view's code
	success_url = '/account/login'
	form_class = PasswordResetRequestForm
	@staticmethod
	def validate_email_address(email):
		try:
			validate_email(email)
			return True
		except ValidationError:
			return False
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			data= form.cleaned_data["email_or_username"]
		if self.validate_email_address(data) is True:                 #uses the method written above
			'''
			If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
			'''
			associated_users= User.objects.filter(Q(email=data)|Q(username=data))
			if associated_users.exists():
				for user in associated_users:
						c = {
							'email': user.email,
							'domain': request.META['HTTP_HOST'],
							'site_name': 'your site',
							'uid': urlsafe_base64_encode(force_bytes(user.pk)),
							'user': user,
							'token': default_token_generator.make_token(user),
							'protocol': 'http',
							}
						subject_template_name='registration/password_reset_subject.txt' 
						# copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
						email_template_name='registration/password_reset_email.html'    
						# copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
						subject = loader.render_to_string(subject_template_name, c)
						# Email subject *must not* contain newlines
						subject = ''.join(subject.splitlines())
						email = loader.render_to_string(email_template_name, c)
						send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
				result = self.form_valid(form)
				messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
				return result
			result = self.form_invalid(form)
			messages.error(request, 'No user is associated with this email address')
			return result
		else:
			'''
			If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
			'''
			associated_users= User.objects.filter(username=data)
			if associated_users.exists():
				for user in associated_users:
					c = {
						'email': user.email,
						'domain': 'example.com', #or your domain
						'site_name': 'example',
						'uid': urlsafe_base64_encode(force_bytes(user.pk)),
						'user': user,
						'token': default_token_generator.make_token(user),
						'protocol': 'http',
						}
					subject_template_name='registration/password_reset_subject.txt'
					email_template_name='registration/password_reset_email.html'
					subject = loader.render_to_string(subject_template_name, c)
					# Email subject *must not* contain newlines
					subject = ''.join(subject.splitlines())
					email = loader.render_to_string(email_template_name, c)
					send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
				result = self.form_valid(form)
				messages.success(request, 'Email a sido enviado a' + data +"'s direccion de correo. por favor revise su imbox para continuar con el registro.")
				return result
			result = self.form_invalid(form)
			messages.error(request, 'Este Username no existe en el sistema.')
			return result
		messages.error(request, 'Invalid Input')
		return self.form_invalid(form)

class PasswordResetConfirmView(FormView):
	template_name = "test_template.html"
	success_url = '/admin/'
	form_class = SetPasswordForm

	def post(self, request, uidb64=None, token=None, *arg, **kwargs):
		"""
		View that checks the hash in a password reset link and presents a
		form for entering a new password.
		"""
		UserModel = get_user_model()
		form = self.form_class(request.POST)
		assert uidb64 is not None and token is not None  # checked by URLconf
		try:
			uid = urlsafe_base64_decode(uidb64)
			user = UserModel._default_manager.get(pk=uid)
		except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
			user = None

		if user is not None and default_token_generator.check_token(user, token):
			if form.is_valid():
				new_password= form.cleaned_data['new_password2']
				user.set_password(new_password)
				user.save()
				messages.success(request, 'Password fue reiniciado.')
				return self.form_valid(form)
			else:
				messages.error(request, 'Password no pudo cambiarse.')
				return self.form_invalid(form)
		else:
			messages.error(request,'El enlace de reinicio ya no es valido.')
			return self.form_invalid(form)