from django.shortcuts import render
from django.views import View

# Create your views here.
from gviews.models import Cat
from gviews.models import Horse

class CatListView(View):
    def get(self, request):
        gatos = Cat.objects.all()
        cats = {"listagatos":gatos}
        print(cats)
        return render(request, 'gviews/cat_list.html', cats)
    
class CatDetailView(View):
    def get(self, request, cat_id):
        gato = Cat.objects.get(pk=cat_id)
        cntx = {"gato":gato}
        return render(request, 'gviews/cat_details.html', cntx)
    
#Vistas usando generic views...
from django.views import generic

class HorseListView(generic.ListView):
    model = Horse

class HorseDetailView(generic.DetailView):
    model = Horse

    

