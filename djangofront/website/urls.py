from django.urls import path
from . import views

urlpatterns = [
    path('', views.holaMundo, name='index'),
    path('bio', views.bio, name='bio'),
    path('page', views.page, name='page')
]