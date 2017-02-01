from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from eleccion import views
from eleccion.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
	url(r'^login/', views.usuarioLogin, name='Login'),
	url(r'^logout/', views.usuarioLogout, name='Logout'),
	url(r'^circunscripciones/', listarCir.as_view(), name='Listar Cir'),
	url(r'^crearCir/', crearCir.as_view(), name='Crear Cir'),
	url(r'^updateCir/(?P<pk>[\w-]+)$', CirUpdate.as_view(), name='Editar Cir'),
	url(r'^deleteCir/(?P<pk>[\w-]+)$', DeleteCir.as_view(), name='Borrar Cir'),
	url(r'^circunscripcion/(?P<circunscripcion_id>\d+)', views.verCir, name='Ver Cir'),
	url(r'^mesa/(?P<mesa_id>\d+)', views.verMesa, name='Ver Mesa'),
	url(r'^editarMesa/(?P<mesa_id>\d+)', views.editarMesa, name='Editar Mesa'),
	url(r'^borrarMesa/(?P<mesa_id>\d+)', views.borrarMesa, name='Borrar Mesa'),
	url(r'^addMesa/(?P<circunscripcion_id>\d+)', views.editarCir, name='add Mesa'),
	
]