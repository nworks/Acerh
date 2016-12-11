from django.shortcuts import render
from vacantes.models import Vacantes, Aplicado
from django.db import models
from django.http import HttpResponseRedirect ,HttpResponse
from django.core import serializers
import json
# Create your views here.
def vacantelist(request):
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

	
	context = { "post":post, "posts":post.all(),"cantidad":cantidad }
	return render(request, 'index2.html', context)

def aplicado(request):
	post = Aplicado.objects.all()
	cantidad = post.count()
	context = { "aplicado":post, "aplicados":post.all() ,"cantidad":cantidad}
	return render(request, 'index3.html', context)


def solicitud(request):
	idview = request.POST.get('id')
	post = Vacantes.objects.get(id=idview)
	solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=1)
	solicit.save()
	return HttpResponse('/vacantes')

def remover(request):
	idview = request.POST.get('id')
	print idview
	post = Aplicado.objects.get(aplico=idview , usuario=request.user) 
	post.delete()
	return HttpResponse('/vacantes')
