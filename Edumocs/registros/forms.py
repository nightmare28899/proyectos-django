from django import forms
from .models import Profesores
from .models import Cursos

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['username','nombre','apellidos','materia','edad']

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['titulo','categoria','duracion','lenguaje','profesor','descripcion','lecciones','precio','imagen'] 
