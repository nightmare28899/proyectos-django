from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Cursos 
from .models import Profesores
from .models import Usuario
from .models import Carrito
from .forms import ProfesoresForm
from .forms import CursosForm
from .forms import UsuariosForm
from .forms import ContactoForm

# Create your views here.
#el login required, pide que se este logeado para poder ingresar a la view, caso contrario redirige al login
@login_required
def carritoView(request):
    username1=request.user.username
    #si el objeto carro esta creado lo regresa con sus datos, caso contrario, solo redirige a la pagina  
    if Carrito.objects.filter(username=username1).exists():
        carro = Carrito.objects.get(username=username1)
        #selecciona del obejto carro, el atributo curso ya que es un many to many
        cursos = carro.curso.all()
        #regresa los cursos y el objeto carro a la vista carrito, devolviendo asi sus datos
        return render(request, "registros/carrito.html",{'cursos':cursos,'carro':carro})
    return render(request,"registros/carrito.html")

def acercade(request):
        return render(request, "registros/acercade.html")

def acercadeRegistro(request):
    if request.method == 'POST':
        form1 = ContactoForm(request.POST)
        if form1.is_valid():#si los datos son correctos
            form1.save()#inserta
            return render(request,'registros/acercade.html')
    form1 = ContactoForm()
    #si algo sale mal se reenvia al formulariolos datos ingresados
    return render(request,"registros/acercade.html",{'form':form1}) 


# Pide que se este logeado para poder ingresar
@login_required
def cursos(request):
    #si el usuario es profesor entonces entra ala pagina cursos profesores
    username1=request.user.username
    #recuepra el usuario
    user = User.objects.get(username=username1)
    #si esta en el grupo de maestros(autorizado solo por el admin) entonces le permitira entrar a cursos maestros 
    if user.groups.filter(name='Profesores').exists():
        #revisa si existe su perfil completo, en caso de no hacerlo lo redirigira a que registre su perfil completo
        if Profesores.objects.filter(username=username1).exists():
            #se obtiene el id del profesor que se usa como llave foranea del curso
            profesor1=Profesores.objects.only('id').get(username=username1).id
            #se filtran los cursos que tengan el nombre del profesor, mostrando unicamente sus cursos
            cursos=Cursos.objects.filter(profesor=profesor1)
            return render(request,"registros/cursosProfesores.html",{'cursos':cursos})
        return render(request,"registros/registroMaestro.html")
    #si el usuario es del grupo usuario entonces entra a la pagina cursos alumno, con sus cursos
    else:
        if Usuario.objects.filter(username=username1).exists():
            cliente=Usuario.objects.get(username=username1)
            cursos=cliente.curso.all()
            #se regresa a la pagina HTML cursos
            return render(request,"registros/cursos.html",{'cursos':cursos})
        return render(request,"registros/cursos.html")

def cursosPlantilla(request, id):
    cursos=Cursos.objects.get(id=id)
    return render(request,"registros/plantilla.html",{'cursos':cursos})

def TodosCursos(request):
    cursos=Cursos.objects.all
    return render(request,"registros/TodosCursos.html",{'cursos':cursos})

def DesarrolloWeb(request):
    cursos=Cursos.objects.filter(categoria="Desarrollo Web")
    return render(request,"registros/DesarrolloWeb.html",{'cursos':cursos})

def Marketing(request):
    cursos=Cursos.objects.filter(categoria="Marketing")
    return render(request,"registros/Marketing.html",{'cursos':cursos})

def Programacion(request):
    cursos=Cursos.objects.filter(categoria="Programacion")
    return render(request,"registros/Programacion.html",{'cursos':cursos})
    
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

def eliminarCurso(request, id, confirmacion='registros/confirmarEliminacion.html'):
    #con el id pide la confirmacion para eliminar el objeto
    curs = get_object_or_404(Cursos, id=id)
    if request.method=='POST':
        curs.delete()
        #se filtran los cursos que tengan el nombre del profesor, mostrando unicamente sus cursos
        username1=request.user.username
        profesor1=Profesores.objects.only('id').get(username=username1).id
        cursos=Cursos.objects.filter(profesor=profesor1)
        return render(request,"registros/cursosProfesores.html",{'cursos':cursos})
    return render(request, confirmacion, {'object':curs})

def catalogo(request):
    cursos=Cursos.objects.filter(titulo="Curso completo de Python 3 de la A a la Z - 2021 +50 horas!")
    #Indicamos el lugar donde se renderizar?? el resultado de esta vista

    return render(request,"registros/catalogo.html",{'cursos':cursos})

@login_required
def formularioCursos(request):
    username1=request.user.username    
    profesor = Profesores.objects.get(username=username1)
    return render(request,"registros/registroCurso.html",{'profesor':profesor})
   
def carrito(request, id):
    username1=request.user.username
    if Usuario.objects.filter(username=username1).exists():
        #si existe el carrito con el username del usuario entra, si no crea su carrito
        if Carrito.objects.filter(username=username1).exists():
            #recupera el objeot carro
            carro = Carrito.objects.get(username=username1)
            #recupera el curso por el id recibido
            curso = Cursos.objects.get(id=id)
            #Se agrega el curso
            carro.curso.add(id)
            if curso in carro.curso.all():
                #se extrae el total del curso
                total = curso.precio
                #se extra el total del carro
                total_carro = carro.total
                #se suma el total del carro con el total del curso
                total_final = total + total_carro
                #se actualiza el nuevo total con el curso a??adido
                carro.total = total_final
                #se guarda el carro
                carro.save()
                cliente=Usuario.objects.get(username=username1)
                cursos=cliente.curso.all()
                return render(request,"registros/cursos.html",{'cursos':cursos})
        #crea el carrito, se agrega el curso que se pidio
        curso = Cursos.objects.get(id=id)
        #se suma al total el curso
        total = curso.precio
        #se crea el carrito
        instance = Carrito.objects.create(total=total,username=username1)
        #se a??ade el curso al carrito
        instance.curso.add(id)
        return render(request,"registros/cursos.html")
    cursos=Cursos.objects.get(id=id)
    return render(request,"registros/registroClientes.html",{'cursos':cursos})


def registroCursos(request):
    if request.method == 'POST':
        form = CursosForm(request.POST,request.FILES)
        if form.is_valid():#si los datos son correctos
            form.save()#inserta
            username1=request.user.username   
            profesor1=Profesores.objects.only('id').get(username=username1).id
            cursos=Cursos.objects.filter(profesor=profesor1)
            return render(request,"registros/cursosProfesores.html",{'cursos':cursos})
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
            group = Group.objects.get(name='Usuarios')
            user.groups.add(group)
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

def clientesRegistro(request):
    if request.method == 'POST':
        form1 = UsuariosForm(request.POST)
        if form1.is_valid():#si los datos son correctos
            form1.save()#inserta
            return render(request,'contenido/index.html')
    form1 = UsuariosForm()
    #si algo sale mal se reenvia al formulariolos datos ingresados
    return render(request,"registros/registroClientes.html",{'form':form1}) 

def registroClientesForm(request, id):
    #recupera el nombre de usuario
    username1=request.user.username
    #si el usuario esta registrado, agrega el curso a su lista de cursos
    if Usuario.objects.filter(username=username1).exists():
        #recupera al cliente
        cliente=Usuario.objects.get(username=username1)
        #agrega el curso
        cliente.curso.add(id)
        #regresa todos los cursos
        cursos=cliente.curso.all()
        return render(request,"registros/cursos.html",{'cursos':cursos})
    #si no esta registrado lo manda a que termine su registro
    cursos=Cursos.objects.get(id=id)
    return render(request,"registros/registroClientes.html",{'cursos':cursos})


def pagar(request, id):
    username1=request.user.username
    carro = Carrito.objects.get(id=id)
    curso = carro.curso.all()
    cliente=Usuario.objects.get(username=username1)
    cliente.curso.add(*curso)
    curs = get_object_or_404(Carrito, id=id)
    curs.delete()
    return render(request,"registros/cursos.html")
    # cliente.curso.add(curso)
    
    