# Formulario para el modelo Producto
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # Incluye los campos actualizados del modelo Producto
        fields = ['nombre', 'tipo', 'precio_venta', 'stock', 'expansion', 'imagen']
        
        # Opcional: Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre de la Carta',
            'tipo': 'Tipo (Pokémon/Entrenador/Energía)',
            'precio_venta': 'Precio de Venta',
            'stock': 'Stock Disponible',
            'expansion': 'Expansión de Origen',
            'imagen': 'Imagen de la Carta',
        }
