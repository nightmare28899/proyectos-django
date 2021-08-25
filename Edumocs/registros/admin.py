from django.contrib import admin
from .models import Profesores
from .models import Cursos
from .models import Usuario
from .models import Carrito
from .models import Contacto

admin.site.register(Profesores)
admin.site.register(Cursos)
admin.site.register(Usuario)
admin.site.register(Carrito)
admin.site.register(Contacto)
