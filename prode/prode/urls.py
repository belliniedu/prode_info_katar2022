from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('mis-grupos/', views.MisGrupos.as_view(),),
    path("cerrar-sesion/",auth_views.LogoutView.as_view(), name="logout")
]
 

