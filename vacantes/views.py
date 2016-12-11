from django.shortcuts import render
from vacantes.models import Vacantes, Aplicado
from django.db import models
from django.http import HttpResponseRedirect ,HttpResponse
# Create your views here.
def vacantelist(request):
	post = Vacantes.objects.all()
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
	solicit =  Aplicado.objects.create(usuario=request.user, aplico_id=post.id, estatus_id=4)
	solicit.save()
	return HttpResponse('/vacantes')

def remover(request):
	idview = request.POST.get('id')
	print idview
	post = Aplicado.objects.get(aplico=idview , usuario=request.user) 
	post.delete()
	return HttpResponse('/vacantes')