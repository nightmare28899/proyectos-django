from django import forms
from .models import Profesores
from .models import Cursos
from .models import Usuario
from .models import Carrito

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['username','nombre','apellidos','materia','edad']

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['titulo','categoria','duracion','lenguaje','profesor','descripcion','lecciones','precio','fecha_inicio','fecha_terminacion','imagen'] 

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','nombre','apellidos','edad','curso']

class CarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['curso','total']