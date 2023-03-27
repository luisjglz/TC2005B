from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def holaMundo(request):
    #return HttpResponse("<h1>Hola mundo</h1><ul><li>A</li><li>B</li></ul>")
    return render(request, "website/holaMundo.html")

def bio(request):
    return render(request, "website/bio.html")

def page(request):
    return render(request, "website/page.html")