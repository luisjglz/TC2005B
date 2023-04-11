from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def crearAlumno(request):
    #POST
    if(request.method == 'POST'):
        form = AlumnoModelForm(request.POST)
        if(form.is_valid()):
            form.save()
            #return HttpResponse('Nuevo alumno creado: ' + form["nombre"].value())
            request.session["msj"] = 'Nuevo alumno creado: ' + form["nombre"].value()
            return redirect(request.path)

    #GET
    #form = CrearAlumnoForm()
    form = AlumnoModelForm
    msg = request.session.get('msj', False)
    if(msg): del(request.session['msj'])
    return render(request, 'website/crearAlumno.html', {'form':form, 'msj':msg})




