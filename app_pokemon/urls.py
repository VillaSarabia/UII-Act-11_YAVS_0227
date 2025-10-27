# Definiciones de URL para la aplicación app_pokemon

from django.urls import path
from . import views

app_name = 'app_pokemon' # Namespace de la aplicación

urlpatterns = [
    # Rutas para PRODUCTOS (Cartas)
    path('', views.listar_productos, name='listar_productos'), # Raíz de la app (Catálogo)
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
    
    # Rutas para EXPANSIONES (Colecciones)
    path('expansiones/', views.listar_expansiones, name='listar_expansiones'),
    path('expansiones/crear/', views.crear_expansion, name='crear_expansion'),
]
