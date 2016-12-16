from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse
from users.forms import LoginForm ,UserP, UsuarioForm2, UserPr
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

@csrf_protect
def LoginRequest(request):
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
				return HttpResponseRedirect('/vacantes')
			# De lo contrario devolver al Login
			else:
				render(request, "login2.html", {'form':form})
				return render(request, "login2.html", {'form':form})
		# Si el formulario es invalido devolver al login
		else:
			return render(request, "login2.html", {'form':form})
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
		profile_form = UserPr(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				profile.file = request.FILES['file']

				profile.save()
				registered = True
				username = user_form.cleaned_data['username']
				password = user_form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				login(request,usuario)
				return HttpResponseRedirect('/vacantes')
			else:
				profile.save()
				registered = True
				username = user_form.cleaned_data['username']
				password = user_form.cleaned_data['password']
				profile.file = request.FILES['file']
				profile.save()
				usuario = authenticate(username=username,password=password)
				login(request,usuario)
				return HttpResponseRedirect('/vacantes')
	else:
		user_form = UsuarioForm2()
		profile_form = UserPr()
        
	return render (request,'index.html',{'user_form':user_form, 'profile_form': profile_form})
