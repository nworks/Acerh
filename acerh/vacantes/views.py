from django.shortcuts import render, redirect
from vacantes.models import Vacante, Aplicado, Area, Preguntado, Provincia, Compania
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
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

@login_required
def vacantelist(request):
	if request.user.is_staff:
		return redirect('/compania')
	result1 = serializers.serialize("json",Aplicado.objects.filter(usuario=request.user.id))
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		array.insert(0,i["fields"]["aplico"])
	
	post = Vacante.objects.exclude(pk__in=array).filter(pais=request.user.userp.pais_apli)

	paginator = Paginator(post, 2) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = Aplicado.objects.filter(usuario=request.user.id).count()
	area = Area.objects.all()
	noficacion = notify.objects.all()





	context = { "noficacion":noficacion,"noficaciones":noficacion.all(),"post":post, "posts":posts,"cantidad":cantidad,"area":area,"areas":area.all() }
	return render(request, 'vacantes.html', context)


def vacantelist2(request):
	if request.user.is_staff:
		return redirect('/compania')
	result1 = serializers.serialize("json",Aplicado.objects.filter(usuario=request.user.id))
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		array.insert(0,i["fields"]["aplico"])
	post = Vacante.objects.exclude(pk__in=array).filter(pais=request.user.userp.pais_apli)
	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = Aplicado.objects.filter(usuario=request.user.id).count()
	area = Area.objects.all()
	noficacion = notify.objects.all()





	context = { "noficacion":noficacion,"noficaciones":noficacion.all(),"post":post, "posts":post.all(),"cantidad":cantidad,"area":area,"areas":area.all() }
	return render(request, 'vacantes2.html', context)


def list_vacant(request, id=None):
	aplicado = Aplicado.objects.filter(aplico=id)
	context = {
		"app":aplicado, "apps":aplicado.all()
	}

	return render(request, 'companiaus.html', context)

@login_required
def aplicado(request):
	post = Aplicado.objects.filter(usuario=request.user.id)
	cantidad = post.count()
	context = { "aplicado":post, "aplicados":post.all() ,"cantidad":cantidad}
	return render(request, 'aplicado.html', context)

@login_required
def aplicado2(request):
	post = Aplicado.objects.filter(usuario=request.user.id)
	cantidad = post.count()
	context = { "aplicado":post, "aplicados":post.all() ,"cantidad":cantidad}
	return render(request, 'aplicado2.html', context)

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
		pais = request.user.userp.pais_apli

		solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=2,respuesta=respuesta1,respuesta2=respuesta2,respuesta3=respuesta3,respuesta4=respuesta4,respuesta5=respuesta5,respuesta6=respuesta6,respuesta7=respuesta7,respuesta8=respuesta8, pais=pais)
		solicit.save()
	else:
		pais = request.user.userp.pais_apli
		solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=2, pais=pais)
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
def compania2(request):
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
	creada = Vacante.objects.filter(compania=request.user)

	context = {"creada":creada,"creadas":creada.all(), "post":post,"usuario":usuario,"usuarios":usuario.all(), "posts":post.all(),"cantidad":cantidad ,"cantidad2":cantidad2,"cantidad3":cantidad3,"cantidad4":cantidad4,"area":area,"areas":area.all()}

	return render(request, 'compania.html', context)

def compania(request):
	contact_list = Vacante.objects.filter(pais=request.user.userp.pais_apli)
	post2 = Aplicado.objects.all()
	cantidad = post2.count()
	cantidad2 = Vacante.objects.filter(compania=request.user).count()
	cantidad3 = Aplicado.objects.filter(usuario=request.user.id).count()
	cantidad4 = Vacante.objects.all().count()
	area = Area.objects.all()
	compania = Compania.objects.all()
	creada = Vacante.objects.filter(compania=request.user)
	paginator = Paginator(contact_list, 10) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	return render(request, 'vacantetabla.html', {'compania': compania,'companias': compania.all(),'posts': posts ,"creada":creada,"creadas":creada.all(), "cantidad":cantidad ,"cantidad2":cantidad2,"cantidad3":cantidad3,"cantidad4":cantidad4,"area":area,"areas":area.all()})

@login_required
def solicitudcompania(request):
	titulo = request.POST.get('titulo')
	area = request.POST.get('area')
	compania = request.POST.get('compania')
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
	print compania
	area2 = Area.objects.get(titulo=area)
	compania2 = Compania.objects.get(titulo=compania)
	pais = request.user.userp.pais_apli
	print pais
	print area2
	print compania
	solicit =  Vacante.objects.create(compania=request.user, titulo=titulo, descripcion=descripcion, area_id=area2.id, requisitos=requisitos,pregunta1=pregunta1,pregunta2=pregunta2,pregunta3=pregunta3,pregunta4=pregunta4,pregunta5=pregunta5,pregunta6=pregunta6,pregunta7=pregunta7,pregunta8=pregunta8, pais=pais, compania2_id=compania2.id)
	solicit.save()
	return HttpResponse('/compania')


@login_required
def removerc(request):
	idview = request.POST.get('id')
	print idview
	post = Vacante.objects.get(id=idview , compania=request.user)
	post.delete()
	return HttpResponse('/vacantes')


from itertools import chain

@login_required
def companiass(request):
	app = Aplicado.objects.filter(~Q(estatus2='Procesado')).filter(pais=request.user.userp.pais_apli)
	are = Area.objects.all()
	prov = Provincia.objects.all()
	entreform = EntrevistaForm(data=request.FILES)

	paginator = Paginator(app, 20) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		apps = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		apps = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		apps = paginator.page(paginator.num_pages)



	if request.method == 'GET':
		if 'nombre' in request.GET:
			nombre = request.GET.get('nombre')

		else:
			nombre = ""
		if 'apellido' in request.GET:
			apellido = request.GET.get('apellido')

		else:
			apellido = ""
		if 'correo' in request.GET:
			correo = request.GET.get('correo')
			
			print correo

		else:
			correo = ""
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

		if 'experiencia' in request.GET:
			experiencia = request.GET.get('experiencia')
		else:
			experiencia = ""

		
		print edad
		lookups =  Q(ar_exp__icontains=experiencia) | Q(carrera__icontains=carrera) | Q(idioma__icontains=idioma) | Q(edad__icontains=edad) 
		lookups1 = Q(first_name__icontains=nombre) | Q(last_name__icontains=apellido) | Q(email__icontains=correo)
		loc1 = User.objects.filter(lookups1).distinct()
		loc = UserP.objects.filter(lookups).distinct()
		
		results = chain(loc,loc1)
		print results

		array = []
		for e in loc:
			array.insert(0,e.user.pk)
		app = Aplicado.objects.filter(~Q(estatus2='Procesado')).filter(pais=request.user.userp.pais_apli).filter(usuario_id__in=array)
		 

		return render(request, 'companiass.html', {"apps":apps, 'entreform':entreform,'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()} )


	elif request.method == 'POST':
		entreform = EntrevistaForm(data=request.POST)
		if entreform.is_valid():
			idview = request.POST.get('id')
			post = Aplicado.objects.get(pk=idview)
			print idview
			if "entrevista" in request.FILES:
				post.entrevista = request.FILES["entrevista"]
			else:
				post.entrevista = static('/nocv.txt')
			post.comentario = request.POST["comentario"]
			post.com_interno = request.POST["com_interno"]
			post.estatus2 = 'Procesado'
			post.save()
			return render(request, 'companiass.html', {"app":app,"apps":app.all(), 'entreform':entreform,'are':are, 'areas':are.all() ,'prov':prov, 'provincias':prov.all()})
		else:
			entreform = EntrevistaForm(data=request.FILES)

	return render(request, 'companiass.html',  {'entreform':entreform,'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()})

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
	app = Aplicado.objects.filter(estatus2='Procesado').filter(pais=request.user.userp.pais_apli)
	are = Area.objects.all()
	prov = Provincia.objects.all()

	paginator = Paginator(app, 20) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		apps = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		apps = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		apps = paginator.page(paginator.num_pages)


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

		if 'pais_apli' in request.GET:
			pais_apli = request.GET.get('pais_apli')
		else:
			pais_apli = ""

		loc = UserP.objects.filter(localidad__icontains=localidad,sexo__icontains=sexo,ar_int__icontains=areaid,ar_exp__icontains=areaid2,carrera__icontains=carrera,idioma__icontains=idioma,edad__icontains=edad,universidad__icontains=universidad,licencia__icontains=licencia,cat_licen__icontains=cat_licen,pais_apli__icontains=pais_apli)
		array = []
		for e in loc:
			array.insert(0,e.user.pk)
		app = Aplicado.objects.filter(estatus2='Procesado').filter(pais=request.user.userp.pais_apli) & Aplicado.objects.filter(usuario_id__in=array)

	return render(request, 'companiaus.html',  {'apps':apps,'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()})

@login_required
def registerusers(request):
	app = Aplicado.objects.filter()
	user = User.objects.filter()
	are = Area.objects.all()
	prov = Provincia.objects.all()
	rdusers = UserP.objects.filter(pais_apli='Republica Dominicana').count()
	salvador = UserP.objects.filter(pais_apli='El Salvador').count()
	guatemala = UserP.objects.filter(pais_apli='Guatemala').count()
	honduras = UserP.objects.filter(pais_apli='Honduras').count()
	jamaica = UserP.objects.filter(pais_apli='Jamaica').count()
	nicaragua = UserP.objects.filter(pais_apli='Nicaragua').count()
	tb = UserP.objects.filter(pais_apli='Trinidad y Tobago').count()

	rdapli = Aplicado.objects.filter(pais='Republica Dominicana').count()
	saapli = Aplicado.objects.filter(pais='El Salvador').count()
	guapli = Aplicado.objects.filter(pais='Guatemala').count()
	hoapli = Aplicado.objects.filter(pais='Honduras').count()
	jaapli = Aplicado.objects.filter(pais='Jamaica').count()
	niapli = Aplicado.objects.filter(pais='Nicaragua').count()
	tbapli = Aplicado.objects.filter(pais='Trinidad y Tobago').count()

	paginator = Paginator(user, 8) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

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

		if 'pais_apli' in request.GET:
			pais_apli = request.GET.get('pais_apli')
		else:
			pais_apli = ""

		loc = UserP.objects.filter(localidad__icontains=localidad).filter(sexo__icontains=sexo).filter(ar_int__icontains=areaid).filter(ar_exp__icontains=areaid2).filter(carrera__icontains=carrera).filter(idioma__icontains=idioma).filter(edad__icontains=edad).filter(universidad__icontains=universidad).filter(licencia__icontains=licencia).filter(cat_licen__icontains=cat_licen).filter(pais_apli__icontains=pais_apli)
		array = []
		for e in loc:
			array.insert(0,e.user.pk)
		user = User.objects.filter(id__in=array)
	return render(request, 'users.html',{'posts': posts,'saapli':saapli,'niapli':niapli,'tbapli':tbapli,'hoapli':hoapli,'jaapli':jaapli,'guapli':guapli,'rdapli':rdapli,'jamaica':jamaica,'tb':tb,'guatemala':guatemala,'nicaragua':nicaragua,'honduras':honduras,'salvador':salvador,'rdusers':rdusers,'user':user, 'users':user.all(),'app':app, 'apps':app.all(),'are':are, 'areas':are.all(),'prov':prov, 'provincias':prov.all()})


def companiapag(request):
	apli_list = Aplicado.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(apli_list, 10)
	try:
		paged = paginator.page(page)
	except PageNotAnInteger:
		paged = paginator.page(1)
	except EmptyPage:
		paged = paginator.page(paginator.num_pages)

	context = { 'paged': paged,"creada":creada,"creadas":creada.all(), "post":post,"usuario":usuario,"usuarios":usuario.all(), "posts":post.all(),"cantidad":cantidad ,"cantidad2":cantidad2,"cantidad3":cantidad3,"cantidad4":cantidad4,"area":area,"areas":area.all()}
	return render(request, 'index4.html', { context })


@csrf_exempt
def vacantejson(request):
	data3 = json.loads(request.body)
	mouser = Token.objects.get(key=data3["token"])
	print mouser
	print mouser.user.id
	result1 = serializers.serialize("json",Aplicado.objects.filter(usuario=mouser.user))
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		array.insert(0,i["fields"]["aplico"])
	print array
	vjs = Vacante.objects.exclude(pk__in=array)
	#print vjs
	Vacantes = []
	for tmpPickUp in vjs:
		titulo=tmpPickUp.titulo
		descripcion=tmpPickUp.descripcion
		postid = tmpPickUp.id
		requisitos = tmpPickUp.requisitos
		pregunta1 = tmpPickUp.pregunta1
		pregunta2 = tmpPickUp.pregunta2
		pregunta3 = tmpPickUp.pregunta3
		pregunta4 = tmpPickUp.pregunta4
		pregunta5 = tmpPickUp.pregunta5
		pregunta6 = tmpPickUp.pregunta6
		pregunta7 = tmpPickUp.pregunta7
		pregunta8 = tmpPickUp.pregunta8
		#print titulo,descripcion,requisitos, postid
		record = {"titulo":titulo, "descripcion":descripcion,"requisitos":requisitos,"postid":postid,  "pregunta2":pregunta2, "pregunta3":pregunta3, "pregunta4":pregunta4 , "pregunta5":pregunta5, "pregunta6":pregunta6, "pregunta7":pregunta7 ,"pregunta8":pregunta8 }
		#print record
		Vacantes.append(record)

		#pickup_records = json.dumps(pickup_records)
		pickup_records = json.dumps(Vacantes)
		pickup_response={"vacantes":Vacantes}
	return JsonResponse(pickup_response , safe=False)



@csrf_exempt
def solcomjs(request):
	data = request
	data1 = request.body
	print data
	print data1
	data3 = json.loads(request.body)
	print data3["post"]
	print data3["estatus"]
	print data3["token"]
	mouser = Token.objects.get(key=data3["token"])
	print mouser.user
	solicit =  Aplicado.objects.create(usuario=mouser.user, aplico_id=data3["post"], estatus_id=2)
	solicit.save()
	return HttpResponse(json.dumps("ok estatus"), content_type='application/json')

@csrf_exempt
def aplicadomov(request):
	#Obtener el usuario del json movil
	data3 = json.loads(request.body)
	print json.loads(request.body)
	mouser = Token.objects.get(key=data3["token"])
	print "mouser" , mouser.user
	vacante_dict = {}
	Aplicados=[]
	vjs = Aplicado.objects.filter(usuario=mouser.user)
	print Aplicado.objects.filter(usuario=mouser.user)
	for tmpPickUp in vjs:
		vacan = Vacante.objects.get(id=tmpPickUp.aplico.id)
		titulo = vacan.titulo
		descripcion = vacan.descripcion

		idpost = tmpPickUp.id
		print idpost
		record = { "idpost":idpost, "titulo":titulo, "descripcion":descripcion}
		print record
		Aplicados.append(record)
		pickup_records = json.dumps(Aplicados)
		pickup_response={"aplicados":Aplicados}


	return JsonResponse(pickup_response, safe=False)

@csrf_exempt
def removermov(request):
	data3 = json.loads(request.body)
	print json.loads(request.body)
	data3["id"]
	mouser = Token.objects.get(key=data3["token"])
	print "mouser" , mouser.user
	post = Aplicado.objects.get(id=data3["id"] , usuario=mouser.user)
	post.delete()
	return HttpResponse(json.dumps("Deleted"), content_type='application/json')


def actualizapais(request):
	app = Aplicado.objects.all().update(pais='Republica Dominicana')

	return HttpResponse('Done')
