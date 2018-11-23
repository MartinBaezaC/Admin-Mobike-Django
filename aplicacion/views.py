from django.shortcuts import render
from .models import Usuario
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def cargarInicio(request):
	return render(request, 'aplicacion/index.html')

def cargarFormulario(request):
	return render(request, 'aplicacion/formulario-usuario.html')

def grabarUsuario(request):
	nombre = request.POST['txtNombre']
	apellido = request.POST['txtApellido']
	rut = request.POST['txtRut']
	comuna = request.POST['txtComuna']
	trabajo = request.POST['txtTrabajo']
	u = Usuario(nombre_usuario = nombre, apellido_usuario = apellido, rut_usuario = rut, comuna_usuaro = comuna, lugar_trabajo = trabajo)
	u.save();
	return render(request, 'aplicacion/grabar-usuario.html',{'nombre' : nombre},{'apellido' : apellido})

def buscarUsuarios(request):
	listadoUsuarios = Usuario.objects.all()
	template = loader.get_template('aplicacion/buscar-usuarios.html')
	context = {
		'usuarios' : listadoUsuarios,
	}
	return HttpResponse(template.render(context, request))

def seguirUsuario(request):
	return render(request, 'aplicacion/seguir-usuario.html')	