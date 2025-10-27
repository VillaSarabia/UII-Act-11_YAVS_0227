# Vistas para la aplicación de Tienda Pokémon

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Expansion
from .forms import ProductoForm
from .expansion_forms import ExpansionForm # ¡CORREGIDO! Importación relativa

# --- Vistas de PRODUCTOS ---

def listar_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, 'listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('app_pokemon:listar_productos')
    else:
        form = ProductoForm()
    
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': 'Crear Nueva Carta (Producto)'})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto) 
        if form.is_valid():
            form.save()
            return redirect('app_pokemon:detalle_producto', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'formulario_producto.html', {'form': form, 'titulo': f'Editar Carta: {producto.nombre}'})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('app_pokemon:listar_productos')
    
    return render(request, 'confirmar_borrar_producto.html', {'producto': producto})


# --- Vistas de EXPANSIONES ---

def listar_expansiones(request):
    expansiones = Expansion.objects.all().order_by('-fecha_lanzamiento')
    return render(request, 'listar_expansiones.html', {'expansiones': expansiones})

def crear_expansion(request):
    if request.method == 'POST':
        form = ExpansionForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('app_pokemon:listar_expansiones') 
    else:
        form = ExpansionForm()
    
    return render(request, 'formulario_expansion.html', {'form': form, 'titulo': 'Crear Nueva Expansión'})
