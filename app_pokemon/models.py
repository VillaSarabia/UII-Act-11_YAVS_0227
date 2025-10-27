# Modelos para la aplicación Tienda Pokémon

from django.db import models

# Modelo para las Expansiones (Tablas Expansiones)
class Expansion(models.Model):
    # ID_expansion se crea automáticamente como 'id'
    nombre_expansion = models.CharField(max_length=150)
    fecha_lanzamiento = models.DateField()
    total_cartas = models.IntegerField(default=0)
    idioma = models.CharField(max_length=50)
    activa = models.BooleanField(default=True) # Indica si la expansión está en circulación o activa

    def __str__(self):
        return f"{self.nombre_expansion} ({self.idioma})"

    class Meta:
        verbose_name = "Expansión"
        verbose_name_plural = "Expansiones"
        ordering = ['-fecha_lanzamiento']


# Modelo para los Productos (Tablas Productos)
class Producto(models.Model):
    # ID_producto se crea automáticamente como 'id'
    nombre = models.CharField(max_length=200) # Nombre de la carta
    tipo = models.CharField(max_length=50) # Ejemplo: Pokémon, Entrenador, Energía
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
    # RELACIÓN: ID_expnasion (ForeignKey a Expansion)
    # on_delete=models.PROTECT evita que se borre una expansión si tiene productos asociados
    expansion = models.ForeignKey(
        Expansion, 
        on_delete=models.PROTECT, 
        related_name='productos',
        null=False # Una carta siempre debe pertenecer a una expansión
    )
    
    # Campo para la imagen de la carta
    imagen = models.ImageField(upload_to='img_productos/', blank=True, null=True) 

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto (Carta)"
        verbose_name_plural = "Productos (Cartas)"
