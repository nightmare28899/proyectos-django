"""Edumocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from contenido import views
from django.conf import settings 
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('carrito/',views_registros.carritoView, name="carritoView"),
    path('acercade/',views.acercade, name="acercade"),
    path('catalogo/',views_registros.catalogo, name="catalogo"),
    path('cursosdisponibles/', views_registros.cursos, name="Cursos"),
    path('login/',views.login, name="login"),
    #Django ofrece un sistema de login, aqui se agrega lo que ofrece el framework entre ellos el login que proporciona al menos en funciones
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/',views_registros.login, name='login'),
    path('registroUsuario/',views_registros.registrarUsuario, name='registroUsuario'),
    path('registroFormulario/',views_registros.registroForm, name='registroUsuarioForm'),
    path('registroProfesor/',views_registros.registroProfesores, name='registroProfesor'),
    path('registroProfesorForm/',views_registros.profesoresRegistro, name='registroProfesorForm'),
    path('registroCursos/',views_registros.formularioCursos, name='registroCurso'),
    path('registroCursosForm/',views_registros.registroCursos, name='registroCursoForm'),
    path('editarCursosForm/<int:id>/',views_registros.editarCursosForm, name='editarCursosForm'),
    path('editarCursos/<int:id>/',views_registros.editarCursos, name='editarCursos'),
    path('eliminarCursos/<int:id>/',views_registros.eliminarCurso, name='eliminarCursos'),
    path('cursos/',views_registros.TodosCursos, name='todoscursos'),
    path('cursos/desarrolloWeb/',views_registros.DesarrolloWeb, name='desarrolloWeb'),
    path('cursos/marketing/',views_registros.Marketing, name='marketing'),
    path('cursos/programacion/',views_registros.Programacion, name='programacion'),
    path('cursos/<int:id>/',views_registros.cursosPlantilla, name='plantillaCursos'),
    path('registro/clientes/<int:id>/',views_registros.registroClientesForm,name='registroClientesForm'),
    path('registroClientes/',views_registros.clientesRegistro, name='registroClientes'),
    path('carrito/<int:id>/',views_registros.carrito, name='carrito'),
    path('pagar/<int:id>/',views_registros.pagar, name='pagar'),
    ]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    