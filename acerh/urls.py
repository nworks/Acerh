"""acerh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users.views import LoginRequest ,LogoutRequest, register,email, ResetPasswordRequestView,PasswordResetConfirmView,consulta, consultauser, user_detail
from vacantes.views import vacantedit, vacantelist, aplicado, solicitud, remover,removerc, compania,companiass, solicitudcompania, passwordrecovery, proceso, preguntas
from users.views import userdetail
from django.conf import settings
from django.conf.urls.static import static
from utils.views import ResetPasswordRequestView, PasswordResetConfirmView

urlpatterns = [
	
					   # url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='reset_password_confirm'), 
					   # PS: url above is going to used for next section of implementation.


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
	from django.conf.urls import patterns, include, url

	urlpatterns = patterns('',
						   url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
							   PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
						   # PS: url above is going to used for next section of
						   # implementation.
						   url(r'^account/reset_password',
							   ResetPasswordRequestView.as_view(), name="reset_password")
						   )

except:
	from django.conf.urls import include, url

	urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^account/reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
			PasswordResetConfirmView.as_view(), name='reset_password_confirm'),
		# PS: url above is going to used for next section of
		# implementation.
	url(r'^account/reset_password',
			ResetPasswordRequestView.as_view()),
	url(r'^admin/', admin.site.urls),
	url(r'^login/',LoginRequest ),
	url(r'^vacantes/',vacantelist ),
	url(r'^aplicado/',aplicado ),
	url(r'logout/', LogoutRequest, name="logout"),
	url(r'register/$', register),
	url(r'^solicitud/', solicitud, name="solicitud"),
	url(r'^proceso/', proceso, name="proceso"),
	url(r'^remover/', remover, name="remover"),
	url(r'^removerc/', removerc, name="removerc"),
	url(r'^compania/',compania ),
	url(r'^companiass/',companiass ),
	url(r'^solicitudcompania/',solicitudcompania ,name="solicitudcompania" ),
	url(r'^userdetail/',userdetail ,name="userdetail" ),
	url(r'^passwordrecovery/',passwordrecovery ,name="passwordrecovery" ),
	url(r'^email/',email ),
	url(r'^preguntas/',preguntas ),
	url(r'^vacantedit/',vacantedit, name="vacantedit"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^consulta/',consulta ),
	url(r'^consultauser/',consultauser ),
	url(r'^user_detail/(?P<id>\d+)/$',user_detail ,name="user_detail"),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




