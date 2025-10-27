from django.contrib import admin
# Importamos los nuevos modelos
from .models import Expansion, Producto 

# Registramos ambos modelos en el panel de administración de Django
admin.site.register(Expansion)
admin.site.register(Producto)
