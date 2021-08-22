from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
        return render(request,"contenido/index.html")

#pide que se este logeado para poder acceder a esa vista.
@login_required
def carrito(request):
        return render(request, "contenido/carrito.html")

def catalogo(request):
        return render(request, "contenido/catalogo.html")

def cursos(request):
        return render(request,"contenido/cursos.html")

def login(request):
        return render(request, "contenido/login.html")

