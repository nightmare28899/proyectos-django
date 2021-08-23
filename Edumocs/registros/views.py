from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Cursos 
from .models import Profesores
from .models import Usuario
from .forms import ProfesoresForm
from .forms import CursosForm

# Create your views here.
# Pide que se este logeado para poder ingresar
@login_required
def cursos(request):
    #si el usuario es profesor entonces entra ala pagina cursos profesores
    username1=request.user.username
    if Profesores.objects.filter(username=username1).exists():
        #se obtiene el id del profesor que se usa como llave foranea del curso
        profesor1=Profesores.objects.only('id').get(username=username1).id
        #se filtran los cursos que tengan el nombre del profesor, mostrando unicamente sus cursos
        cursos=Cursos.objects.filter(profesor=profesor1)
        return render(request,"registros/cursosProfesores.html",{'cursos':cursos})
    #si el usuario es usuario entonces entra ala pagina cursos alumno, con sus cursos
    else:
        if Usuario.objects.filter(username=username1).exists():
            cursos=Cursos.objects.all()
            return render(request,"registros/cursos.html",{'cursos':cursos})
        return render(request,"registros/cursos.html")

def editarCursosForm(request, id):
    username1=request.user.username
    profesor1=Profesores.objects.get(username=username1)
    curso=Cursos.objects.get(id=id)
    return render(request,"registros/cursosEditarForm.html",{'curso':curso,'profesor':profesor1})

def editarCursos(request, id):
    curso = get_object_or_404(Cursos, id=id)
    #identifica por el id el objeto cursos para posteriormente validarlo e incluirlo
    form2 = CursosForm(request.POST,request.FILES, instance=curso)
    if form2.is_valid():
        form2.save()
        username1=request.user.username
        profesor1=Profesores.objects.only('id').get(username=username1).id
        #se filtran los cursos que tengan el nombre del profesor, mostrando unicamente sus cursos
        cursos=Cursos.objects.filter(profesor=profesor1)
        return render(request,"registros/cursosProfesores.html",{'cursos':cursos})

    return render(request,"registros/cursosEditarForm.html",{'curso':curso})

def eliminarCurso(request, id):
    #con el id pide la confirmacion para eliminar el objeto
    curs = get_object_or_404(Cursos, id=id)
    curs.delete()
    username1=request.user.username
    profesor1=Profesores.objects.only('id').get(username=username1).id
        #se filtran los cursos que tengan el nombre del profesor, mostrando unicamente sus cursos
    cursos=Cursos.objects.filter(profesor=profesor1)
    return render(request,"registros/cursosProfesores.html",{'cursos':cursos})



def catalogo(request):
    cursos=Cursos.objects.filter(titulo="Curso completo de Python 3 de la A a la Z - 2021 +50 horas!")
    #Indicamos el lugar donde se renderizará el resultado de esta vista

    return render(request,"registros/catalogo.html",{'cursos':cursos})

@login_required
def formularioCursos(request):
    username1=request.user.username    
    profesor = Profesores.objects.get(username=username1)
    return render(request,"registros/registroCurso.html",{'profesor':profesor})
   
def registroCursos(request):
    if request.method == 'POST':
        form = CursosForm(request.POST,request.FILES)
        if form.is_valid():#si los datos son correctos
            form.save()#inserta
            return render(request,"registros/cursosProfesores.html")
    form = CursosForm()
    #si algo sale mal se reenvia al formulariolos datos ingresados
    return render(request,"registros/registroCurso.html",{'form':form}) 
#ingresa los datos del crud

def login(request):
    return render(request,"registros/login.html")
    
def registroForm(request):
    return render(request,"registros/registroUsuario.html")

@login_required
def registroProfesores(request):
    return render(request,"registros/registroMaestro.html")

def registrarUsuario(request):
    #obtiene de las vistas los datos y posteriormente, crea los usuarios, el modelo lo da Django
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.method == 'POST':
            # Create user and save to the database
            user = User.objects.create_user(username, email , password)
            user.save()
            return render(request,'contenido/index.html')
    return render(request,'registros/registroUsuario.html')

def profesoresRegistro(request):
    if request.method == 'POST':
        form1 = ProfesoresForm(request.POST)
        if form1.is_valid():#si los datos son correctos
            form1.save()#inserta
            return render(request,'contenido/index.html')
    form1 = ProfesoresForm()
    #si algo sale mal se reenvia al formulariolos datos ingresados
    return render(request,"registros/registroMaestro.html",{'form':form1}) 
#ingresa los datos del crud

def consultarDatosMaestro(request):
    username1=request.user.username
    if Profesores.objects.filter(username=username1).exists():
        profesor = Profesores.objects.get(username=username1)
        return render(request,"registros/registroMaestro.html",{'profesor':profesor})
    else:
        return render(request,"registros/cursos.html",{'cursos':cursos})
