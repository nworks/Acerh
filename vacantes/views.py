from django.shortcuts import render
from vacantes.models import Vacante, Aplicado, Area
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


@login_required
def vacantelist(request):
	result1 = serializers.serialize("json",Aplicado.objects.filter(usuario=request.user.id))
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		print decoded_data
		array.insert(0,i["fields"]["aplico"])
		print array, "ARRAY"
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
		print decoded_data
		array.insert(0,i["fields"]["aplico"])
		print array, "ARRAY"
	post = Vacante.objects.exclude(pk__in=array)
	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = post2.count()
	cantidad2 = Vacante.objects.filter(compania=request.user).count()
	cantidad3 = Aplicado.objects.filter(usuario=request.user.id).count()
	area = Area.objects.all()
	context = { "post":post, "posts":post.all(),"cantidad":cantidad ,"cantidad2":cantidad2,"cantidad3":cantidad3,"area":area,"areas":area.all()}
	return render(request, 'index4.html', context)

@login_required
def solicitudcompania(request):
	titulo = request.POST.get('titulo')
	area = request.POST.get('area')
	requisitos = request.POST.get('requisitos')
	descripcion = request.POST.get('descripcion')
	requerimientos = request.POST.get('req')
	area2 = Area.objects.get(titulo=area)
	
	solicit =  Vacante.objects.create(compania=request.user, titulo=titulo, descripcion=descripcion, area_id=area2.id, requisitos=requisitos)
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
	entreform = EntrevistaForm(data=request.FILES)
	if request.method == 'POST':
		entreform = EntrevistaForm(data=request.POST)
		if entreform.is_valid():
			idview = request.POST.get('id')
			post = Aplicado.objects.get(pk=idview)
			print idview
			post.entrevista = request.FILES["entrevista"]
			post.comentario = request.POST["comentario"]
			post.estatus2 = 'Procesado'
			post.save()
			return render(request, 'index5.html', {"app":app,"apps":app.all(), 'entreform':entreform})
		else:
			entreform = EntrevistaForm(data=request.FILES)

	return render(request, 'index5.html', {"app":app,"apps":app.all(), 'entreform':entreform})

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
		entreform.entrevista = request.FILES['entrevista']
		entreform.save()
		post.estatus2 = "Procesado"
		post.comentario = request.POST.get('comentario')
		post.save()

	return HttpResponse('/companiass')