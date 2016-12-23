from django.shortcuts import render
from vacantes.models import Vacantes, Aplicado
from django.db import models
from django.http import HttpResponseRedirect ,HttpResponse
from django.core import serializers
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def vacantelist(request):
	result1 = serializers.serialize("json",Aplicado.objects.filter(usuario=request.user))
	decoded_data = json.loads(result1)
	array = []
	for i in decoded_data:
		print decoded_data
		array.insert(0,i["fields"]["aplico"])
		print array, "ARRAY"
	post = Vacantes.objects.exclude(pk__in=array)
	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = post2.count()
	

	
	context = { "post":post, "posts":post.all(),"cantidad":cantidad }
	return render(request, 'index2.html', context)

@login_required
def aplicado(request):
	post = Aplicado.objects.all()
	cantidad = post.count()
	context = { "aplicado":post, "aplicados":post.all() ,"cantidad":cantidad}
	return render(request, 'index3.html', context)

@login_required
def solicitud(request):
	idview = request.POST.get('id')
	post = Vacantes.objects.get(id=idview)
	solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=1)
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
	post = Vacantes.objects.exclude(pk__in=array)
	postall = post.all()
	post2 = Aplicado.objects.all()
	cantidad = post2.count()
	cantidad2 = Vacantes.objects.filter(compania=request.user).count()
	cantidad3 = Aplicado.objects.all().count()
	context = { "post":post, "posts":post.all(),"cantidad":cantidad ,"cantidad2":cantidad2,"cantidad3":cantidad3}
	return render(request, 'index4.html', context)

@login_required
def solicitudcompania(request):
	titulo = request.POST.get('titulo')
	descripcion = request.POST.get('descripcion')
	requerimientos = request.POST.get('req')
	solicit =  Vacantes.objects.create(compania=request.user, titulo=titulo, descripcion=descripcion, area_id=1)
	solicit.save()
	return HttpResponse('/compania')


@login_required
def removerc(request):
	idview = request.POST.get('id')
	print idview
	post = Vacantes.objects.get(id=idview , compania=request.user) 
	post.delete()
	return HttpResponse('/vacantes')

@login_required
def companiass(request):
	app = Aplicado.objects.all()
	context = { "app":app,"apps":app.all()}
	return render(request, 'index5.html', context)