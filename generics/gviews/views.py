from django.shortcuts import render
from django.views import View

# Create your views here.
from gviews.models import Cat

class CatListView(View):
    def get(self, request):
        return render(request, 'gviews/cat_list.html')
    
class CatDetailView(View):
    def get(self, request, cat_id):
        print(cat_id)
        nombre = "Luis"
        ctx = {"id_cat": cat_id, "name": nombre}
        return render(request, 'gviews/cat_details.html', ctx)
    
