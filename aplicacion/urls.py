from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.cargarInicio, name='cargarInicio'),
    path('inicio/formulario', views.cargarFormulario, name='cargarFormulario'),
    path('inicio/grabar-usuario', views.grabarUsuario, name='grabarUsuario'),
    path('inicio/seguir', views.seguirUsuario, name='seguirUsuario}'),

]