from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="home"),
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    #path('mis-grupos/', views.MisGrupos.as_view(),),
    path("cerrar-sesion/",auth_views.logout_then_login, name="logout"),
    path('mis-grupos/', views.mis_grupos, name="mis-grupos"),
    #Includes
    path("equipos/", include("equipos.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("grupos/", include("grupos.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

