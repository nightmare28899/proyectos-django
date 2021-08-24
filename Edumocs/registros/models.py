from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField 

# Create your models here.
class Profesores(models.Model):#Define la estructura de la tabla
    id = models.AutoField(primary_key=True, verbose_name='Clave Profesor')
    username = models.TextField(null=True)
    nombre = models.TextField()  
    apellidos = models.TextField()
    materia = models.TextField()
    edad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registro") 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo
    def __str__(self):
        return self.nombre
        #indica el nombre del alumno, no el objeto

class Cursos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    titulo = models.TextField(verbose_name="Nombre Curso")    
    categoria = models.CharField(max_length=50)
    duracion = models.IntegerField(verbose_name="Duracion en Horas")
    lenguaje = models.CharField(null=True, max_length=25)
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE,verbose_name='Profesor')
    descripcion = RichTextField(null=True)
    lecciones =  RichTextField(null=True)
    precio = models.DecimalField(null=True, max_digits=6, decimal_places=0,verbose_name="Costo")
    fecha_inicio = models.DateField(null=True)
    fecha_terminacion = models.DateField(null=True)
    imagen = models.ImageField(null=True,upload_to="media",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registro")
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo
    def __str__(self):
        return self.titulo
        #indica el nombre del alumno, no el objeto

class Usuario(models.Model):#Define la estructura de la tabla
    id = models.AutoField(primary_key=True, verbose_name='Clave Usuario')
    username = models.TextField(null=True)
    nombre = models.TextField()  
    apellidos = models.TextField()
    edad = models.IntegerField()
    curso = models.ManyToManyField(Cursos, help_text="Seleccione los Cursos a cursar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registro") 
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo
    def __str__(self):
        return self.nombre
        #indica el nombre del alumno, no el objeto

class Carrito(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave Usuario')
    username = models.TextField(null=True)
    curso = models.ManyToManyField(Cursos, help_text="Seleccione los Cursos a cursar")
    total = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registro") 
   
