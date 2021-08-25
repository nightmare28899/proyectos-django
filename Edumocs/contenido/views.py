from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
        return render(request,"contenido/index.html")

def catalogo(request):
        return render(request, "contenido/catalogo.html")

def cursos(request):
        return render(request,"contenido/cursos.html")

def login(request):
        return render(request, "contenido/login.html")

