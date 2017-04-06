from django.shortcuts import render
from vacantes.models import Vacante, Aplicado, Area, Preguntado, Provincia
from users.models import UserP
from django.db import models
from users.models import notify
from django.http import HttpResponseRedirect ,HttpResponse
from django.core import serializers
import json
from vacantes.forms import EntrevistaForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from users.models import UserPC, UserP
from django.contrib.auth.models import User


@login_required
def vacantelist(request):
	result1 = serializers.serialize("json",Aplicado.objects.filter(usuario=request.user.id))
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		array.insert(0,i["fields"]["aplico"])
	post = Vacante.objects.exclude(pk__in=array)
	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = Aplicado.objects.filter(usuario=request.user.id).count()
	area = Area.objects.all()
	noficacion = notify.objects.all()

	
	context = { "noficacion":noficacion,"noficaciones":noficacion.all(),"post":post, "posts":post.all(),"cantidad":cantidad,"area":area,"areas":area.all() }
	return render(request, 'index2.html', context)

@login_required
def aplicado(request):
	post = Aplicado.objects.filter(usuario=request.user.id)
	cantidad = post.count()
	context = { "aplicado":post, "aplicados":post.all() ,"cantidad":cantidad}
	return render(request, 'index3.html', context)

@login_required
def solicitud(request):
	idview = request.POST.get('id')
	post = Vacante.objects.get(id=idview)
	if 'respuesta1' in request.POST:
		respuesta1 = request.POST.get('respuesta1')
		respuesta2 = request.POST.get('respuesta2')
		respuesta3 = request.POST.get('respuesta3')
		respuesta4 = request.POST.get('respuesta4')
		respuesta5 = request.POST.get('respuesta5')
		respuesta6 = request.POST.get('respuesta6')
		respuesta7 = request.POST.get('respuesta7')
		respuesta8 = request.POST.get('respuesta8')

		solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=2,respuesta=respuesta1,respuesta2=respuesta2,respuesta3=respuesta3,respuesta4=respuesta4,respuesta5=respuesta5,respuesta6=respuesta6,respuesta7=respuesta7,respuesta8=respuesta8)
		solicit.save()
	else:
		solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=2)
		solicit.save()
	return HttpResponse('/vacantes')

@login_required
def remover(request):
	idview = request.POST.get('id')
	print idview
	post = Aplicado.objects.get(aplico=idview , usuario=request.user) 
	post.delete()
	return HttpResponse('/vacantes')

@login_required
def compania(request):
	result1 = serializers.serialize("json",Aplicado.objects.all())
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		
		array.insert(0,i["fields"]["aplico"])
		
	post = Vacante.objects.all()
	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = post2.count()
	cantidad2 = Vacante.objects.filter(compania=request.user).count()
	cantidad3 = Aplicado.objects.filter(usuario=request.user.id).count()
	cantidad4 = Vacante.objects.all().count()
	area = Area.objects.all()
	usuario = User.objects.all()
	
	context = { "post":post,"usuario":usuario,"usuarios":usuario.all(), "posts":post.all(),"cantidad":cantidad ,"cantidad2":cantidad2,"cantidad3":cantidad3,"cantidad4":cantidad4,"area":area,"areas":area.all()}

	return render(request, 'index4.html', context)

@login_required
def solicitudcompania(request):
	titulo = request.POST.get('titulo')
	area = request.POST.get('area')
	requisitos = request.POST.get('requisitos')
	pregunta1 = request.POST.get('pregunta1')
	pregunta2 = request.POST.get('pregunta2')
	pregunta3 = request.POST.get('pregunta3')
	pregunta4 = request.POST.get('pregunta4')
	pregunta5 = request.POST.get('pregunta5')
	pregunta6 = request.POST.get('pregunta6')
	pregunta7 = request.POST.get('pregunta7')
	pregunta8 = request.POST.get('pregunta8')
	descripcion = request.POST.get('descripcion')
	requerimientos = request.POST.get('req')
	area2 = Area.objects.get(titulo=area)
	
	solicit =  Vacante.objects.create(compania=request.user, titulo=titulo, descripcion=descripcion, area_id=area2.id, requisitos=requisitos,pregunta1=pregunta1,pregunta2=pregunta2,pregunta3=pregunta3,pregunta4=pregunta4,pregunta5=pregunta5,pregunta6=pregunta6,pregunta7=pregunta7,pregunta8=pregunta8)
	solicit.save()
	return HttpResponse('/compania')


@login_required
def removerc(request):
	idview = request.POST.get('id')
	print idview
	post = Vacante.objects.get(id=idview , compania=request.user) 
	post.delete()
	return HttpResponse('/vacantes')

@login_required
def companiass(request):
	app = Aplicado.objects.filter(~Q(estatus2='Procesado'))
	are = Area.objects.all()
	prov = Provincia.objects.all()
	entreform = EntrevistaForm(data=request.FILES)
	if request.method == 'GET':
		if 'localidad' in request.GET:
			localidad = request.GET.get('localidad')
			
		else:
			localidad = "" 
		if 'sexo' in request.GET:
			sexo = request.GET.get('sexo')
			
		else:
			sexo = ""
		if 'ar_int' in request.GET:
			ar_int = request.GET.get('ar_int')
			print ar_int
			areaid =  Area.objects.get(titulo=ar_int)
			print areaid
			
		else:
			areaid = ""
		if 'ar_exp' in request.GET:
			ar_exp = request.GET.get('ar_exp')
			areaid2 =  Area.objects.get(titulo=ar_exp)
			print areaid2
			
		else:
			areaid2 = ""
		if 'carrera' in request.GET:
			carrera = request.GET.get('carrera')
			
		else:
			carrera = ""
		if 'idioma' in request.GET:
			idioma = request.GET.get('idioma')
			
		else:
			idioma = ""
		if 'edad' in request.GET:
			edad = request.GET.get('edad')
		else:
			edad = ""

		loc = UserP.objects.filter(localidad__icontains=localidad).filter(sexo__icontains=sexo).filter(ar_int__icontains=areaid).filter(ar_exp__icontains=areaid2).filter(carrera__icontains=carrera).filter(idioma__icontains=idioma).filter(edad__icontains=edad)
		array = []
		for e in loc:
			array.insert(0,e.user.pk)
		app = Aplicado.objects.filter(~Q(estatus2='Procesado')) & Aplicado.objects.filter(usuario_id__in=array)
			
		return render(request, 'index5.html', {"app":app,"apps":app.all(), 'entreform':entreform,'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()} )
	

	elif request.method == 'POST':
		entreform = EntrevistaForm(data=request.POST)
		if entreform.is_valid():
			idview = request.POST.get('id')
			post = Aplicado.objects.get(pk=idview)
			print idview
			post.entrevista = request.FILES["entrevista"]
			post.comentario = request.POST["comentario"]
			post.com_interno = request.POST["com_interno"]
			post.estatus2 = 'Procesado'
			post.save()
			return render(request, 'index5.html', {"app":app,"apps":app.all(), 'entreform':entreform,'are':are, 'areas':are.all() ,'prov':prov, 'provincias':prov.all()})
		else:
			entreform = EntrevistaForm(data=request.FILES)

	return render(request, 'index5.html',  {'entreform':entreform,'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()})

def passwordrecovery(request):
	app = Aplicado.objects.all()
	context = { "app":app,"apps":app.all()}
	return render(request, 'password-reset.html', context)

from django.shortcuts import get_object_or_404

@login_required
def proceso(request):
	idview = request.POST.get('id')
	print idview
	post = Aplicado.objects.get(pk=idview)
	
	if 'entrevista' in request.FILES:
		entreform.entrevista = request.FILES['entrevista']
		entreform.save()
		post.estatus2 = "Procesado"
		post.comentario = request.POST.get('comentario')
		
		post.save()
	else:
		entreform.save()
		post.estatus2 = "Procesado"
		post.comentario = request.POST.get('comentario')
		post.save()

	return HttpResponse('/companiass')

from smtplib import SMTPRecipientsRefused
from django.core.mail import EmailMultiAlternatives
from django.core.mail.message import EmailMessage

@login_required
def preguntas(request):
	post = Aplicado.objects.filter(usuario=request.user.id)
	vac = Vacante.objects.all()
	vacan = Vacante.objects.filter(compania=request.user)
	array = []
	for e in vacan:
		array.insert(0,e.titulo)

	preg = Preguntado.objects.filter(titulo__in=array)
	cantidad = post.count()
	context = { "aplicado":post, "aplicados":post.all() ,"vac":vac, "vacs":vac.all() ,"cantidad":cantidad, "preg":preg , "preguntas":preg.all()}

	if 'titulomodal' in request.POST:
		if request.method == 'POST':
		    titulomo = request.POST.get('titulomodal')
		    preguntamodal = request.POST.get('preguntamodal')
		    destinatariou = request.POST.get('destinatario')
		 
		    solicit =  Preguntado.objects.create(emisor=request.user, destinatario=request.user, pregunta=preguntamodal, titulo=titulomo, estatus="espera")
		    solicit.save()

	if 'titulo' in request.POST:
		titulo = request.POST.get('titulo')
		mensaje = "El usuario"+ " " +request.user.username + " " + "ha realizado la siguiente pregunta: "+ " " + request.POST.get('mensaje') + ", " + "Favor responder este correo a esta direccion:" + " " + request.user.email
		email = EmailMessage()
		email.subject = titulo
		email.body = mensaje
		email.to = [ "seleccion@acerhempleos.com"]
		email.send()
	

	return render(request, 'preguntas.html', context)


@login_required
def vacantedit(request):
	idview = request.POST.get('id')
	print idview
	post = Vacante.objects.get(pk=idview)
	post.titulo = request.POST.get('titulo')
	post.descripcion = request.POST.get('descripcion')
	post.pregunta1 = request.POST.get('pregunta1')
	post.pregunta2 = request.POST.get('pregunta2')
	post.pregunta3 = request.POST.get('pregunta3')
	post.pregunta4 = request.POST.get('pregunta4')
	post.pregunta5 = request.POST.get('pregunta5')
	post.pregunta6 = request.POST.get('pregunta6')
	post.pregunta7 = request.POST.get('pregunta7')
	post.pregunta8 = request.POST.get('pregunta8')
	post.requisitos = request.POST.get('requisitos')
	area = request.POST.get('area')
	area2 = Area.objects.get(titulo=area)
	post.area = area2
	post.save()



	return HttpResponse('/companiass')

@login_required
def companiaus(request):
	app = Aplicado.objects.filter(estatus2='Procesado')
	are = Area.objects.all()
	prov = Provincia.objects.all()
	if request.method == 'GET':
		if 'localidad' in request.GET:
			localidad = request.GET.get('localidad')
			
		else:
			localidad = "" 
		if 'sexo' in request.GET:
			sexo = request.GET.get('sexo')
			
		else:
			sexo = ""
		if 'ar_int' in request.GET:
			ar_int = request.GET.get('ar_int')
			print ar_int
			areaid =  Area.objects.get(titulo=ar_int)
			print areaid
			
		else:
			areaid = ""
		if 'ar_exp' in request.GET:
			ar_exp = request.GET.get('ar_exp')
			areaid2 =  Area.objects.get(titulo=ar_exp)
			print areaid2
			
		else:
			areaid2 = ""
		if 'carrera' in request.GET:
			carrera = request.GET.get('carrera')
			
		else:
			carrera = ""
		if 'idioma' in request.GET:
			idioma = request.GET.get('idioma')
			
		else:
			idioma = ""
		if 'edad' in request.GET:
			edad = request.GET.get('edad')
		else:
			edad = ""

		if 'universidad' in request.GET:
			universidad = request.GET.get('universidad')
		else:
			universidad = ""

		if 'licencia' in request.GET:
			licencia = request.GET.get('licencia')
		else:
			licencia = ""
		
		if 'cat_licen' in request.GET:
			cat_licen = request.GET.get('cat_licen')
		else:
			cat_licen = ""

		loc = UserP.objects.filter(localidad__icontains=localidad).filter(sexo__icontains=sexo).filter(ar_int__icontains=areaid).filter(ar_exp__icontains=areaid2).filter(carrera__icontains=carrera).filter(idioma__icontains=idioma).filter(edad__icontains=edad).filter(universidad__icontains=universidad).filter(licencia__icontains=licencia).filter(cat_licen__icontains=cat_licen)
		array = []
		for e in loc:
			array.insert(0,e.user.pk)
		app = Aplicado.objects.filter(estatus2='Procesado') & Aplicado.objects.filter(usuario_id__in=array)
		
	return render(request, 'index6.html',  {'app':app, 'apps':app.all(),'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()})

@login_required
def registerusers(request):
	app = Aplicado.objects.filter()
	user = User.objects.filter()
	are = Area.objects.all()
	prov = Provincia.objects.all()
	
	if request.method == 'GET':
		if 'localidad' in request.GET:
			localidad = request.GET.get('localidad')
			
		else:
			localidad = "" 
		if 'sexo' in request.GET:
			sexo = request.GET.get('sexo')
			
		else:
			sexo = ""
		if 'ar_int' in request.GET:
			ar_int = request.GET.get('ar_int')
			print ar_int
			areaid =  Area.objects.get(titulo=ar_int)
			print areaid
			
		else:
			areaid = ""
		if 'ar_exp' in request.GET:
			ar_exp = request.GET.get('ar_exp')
			areaid2 =  Area.objects.get(titulo=ar_exp)
			print areaid2
			
		else:
			areaid2 = ""
		if 'carrera' in request.GET:
			carrera = request.GET.get('carrera')
			
		else:
			carrera = ""
		if 'idioma' in request.GET:
			idioma = request.GET.get('idioma')
			
		else:
			idioma = ""
		if 'edad' in request.GET:
			edad = request.GET.get('edad')
		else:
			edad = ""

		if 'universidad' in request.GET:
			universidad = request.GET.get('universidad')
		else:
			universidad = ""

		if 'licencia' in request.GET:
			licencia = request.GET.get('licencia')
		else:
			licencia = ""
		
		if 'cat_licen' in request.GET:
			cat_licen = request.GET.get('cat_licen')
		else:
			cat_licen = ""

		loc = UserP.objects.filter(localidad__icontains=localidad).filter(sexo__icontains=sexo).filter(ar_int__icontains=areaid).filter(ar_exp__icontains=areaid2).filter(carrera__icontains=carrera).filter(idioma__icontains=idioma).filter(edad__icontains=edad).filter(universidad__icontains=universidad).filter(licencia__icontains=licencia).filter(cat_licen__icontains=cat_licen)
		array = []
		for e in loc:
			array.insert(0,e.user.pk)
		user = User.objects.filter(id__in=array)
		
	return render(request, 'users.html',  {'user':user, 'users':user.all(),'app':app, 'apps':app.all(),'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()})