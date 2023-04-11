from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

#cRud = enlistar alumnos (usando generic views)

class AlumnoListView(ListView):
    model = Alumno
    template_name = 'website/alumnos.html'
    context_object_name = 'alumnos'


class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'website/alumno.html'
    context_object_name = 'alumno'


class AlumnoCreateView(CreateView):
    model = Alumno
    template_name = 'website/create_edit.html'
    fields = ['nombre', 'grupo', 'activo']
    success_url = '/lista_alumnos'

class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = 'website/create_edit.html'
    fields = ['nombre', 'grupo', 'activo']
    success_url = '/lista_alumnos'


class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'website/confirm.html'
    success_url = '/lista_alumnos'