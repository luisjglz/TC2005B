from django.urls import path
from .views import *

urlpatterns = [
    path('lista_alumnos', AlumnoListView.as_view(), name='alumnos'),
    path('detalles_alumno/<int:pk>', AlumnoDetailView.as_view(), name='detalles_alumno'),
    path('alumno/add', AlumnoCreateView.as_view(), name='add_alumno'),
    path('alumno/<int:pk>', AlumnoUpdateView.as_view(), name='edit_alumno'),
    path('alumno/delete/<int:pk>/', AlumnoDeleteView.as_view(), name='delete_alumno'),
]
