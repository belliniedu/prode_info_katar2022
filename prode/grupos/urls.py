from django.urls import path
from . import views


app_name = "grupos"

urlpatterns = [
	path("listar/", views.Listar.as_view(), name="listar"),
	path("crear/", views.Crear.as_view(), name="crear"),
	path("ver/<int:pk>/", views.ver, name="ver"),
	path("inscribirme/<int:id_usuario>/<int:id_grupo>", views.inscripciones, name="inscribirme")
	]
