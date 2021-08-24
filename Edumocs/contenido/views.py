from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
        return render(request,"contenido/index.html")

def acercade(request):
        return render(request, "contenido/acercade.html")
#pide que se este logeado para poder acceder a esa vista.


def catalogo(request):
        return render(request, "contenido/catalogo.html")

def cursos(request):
        return render(request,"contenido/cursos.html")

def login(request):
        return render(request, "contenido/login.html")

