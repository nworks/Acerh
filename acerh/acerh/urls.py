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
from users.views import LoginRequest ,LogoutRequest, register,email, ResetPasswordRequestView,PasswordResetConfirmView,consulta, consultauser, user_detail, consultaur,export_excel, export_excel2, logouttk
from vacantes.views import vacantedit, vacantelist, aplicado, solicitud, remover,removerc, compania,companiass,companiaus, solicitudcompania, passwordrecovery, proceso, preguntas,registerusers, list_vacant,vacantejson,solcomjs
from users.views import userdetail
from django.conf import settings
from django.conf.urls.static import static
from utils.views import ResetPasswordRequestView, PasswordResetConfirmView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.views import login, logout



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



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
	url(r'^$',LoginRequest ),
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
	url(r'^solcomjs/',solcomjs ,name="solcomjs" ),
	url(r'^userdetail/',userdetail ,name="userdetail" ),
	url(r'^passwordrecovery/',passwordrecovery ,name="passwordrecovery" ),
	url(r'^email/',email ),
	url(r'^preguntas/',preguntas ),
	url(r'^vacantedit/',vacantedit, name="vacantedit"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^consulta/',consulta ),
	url(r'^consultaur/',consultaur, name="consultaur" ),
	url(r'^consultauser/',consultauser ),
	url(r'^companiaus/',companiaus ),
	url(r'^registerusers/',registerusers ),
	url(r'^user_detail/(?P<id>\d+)/$',user_detail ,name="user_detail"),
	url(r'^vaca_apli/(?P<id>\d+)/$',list_vacant ,name="list_vacant"),
	url(r'^excel/$', export_excel ,name="export_excel"),
	url(r'^excel2/$', export_excel2 ,name="export_excel2"),
	url(r'^vacantejson/',vacantejson ),
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^logouttk/', logouttk.as_view()),
 

	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




