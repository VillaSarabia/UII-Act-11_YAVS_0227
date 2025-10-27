# Formulario para el modelo Expansion (Nuevo archivo)
from django import forms
from .models import Expansion

class ExpansionForm(forms.ModelForm):
    class Meta:
        model = Expansion
        # Incluye todos los campos de Expansión
        fields = ['nombre_expansion', 'fecha_lanzamiento', 'total_cartas', 'idioma', 'activa']
        
        # Opcional: Widgets para mejor UX (especialmente para la fecha)
        widgets = {
            'fecha_lanzamiento': forms.DateInput(attrs={'type': 'date'}),
        }
        
        # Opcional: Etiquetas personalizadas para el formulario
        labels = {
            'nombre_expansion': 'Nombre de la Colección',
            'fecha_lanzamiento': 'Fecha de Lanzamiento',
            'total_cartas': 'Total de Cartas en el Set',
            'idioma': 'Idioma Principal',
            'activa': '¿Está Activa (En Circulación)?',
        }
