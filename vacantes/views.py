from django.shortcuts import render
from vacantes.models import Vacantes, Aplicado
# Create your views here.
def vacantelist(request):
	post = Vacantes.objects.all()
	context = { "post":post, "posts":post.all() }
	return render(request, 'index2.html', context)

def aplicado(request):
	post = Aplicado.objects.all()
	context = { "aplicado":post, "aplicados":post.all() }
	return render(request, 'index3.html', context)
