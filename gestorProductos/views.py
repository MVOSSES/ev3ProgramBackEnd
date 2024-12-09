from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from gestorProductos.forms import CategoriaForm, ProductoForm
from gestorProductos.models import Categoria, Producto

# Create your views here.
#vista Categoría
def categoriaData(request): 
    categorias = Categoria.objects.all()
    data = {
        'categorias': categorias
    }
    return render(request, 'gestorProductos/categoriaVer.html', data)

#vista producto
def productoData(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'gestorProductos/productoVer.html', data)

#vista categoriaRegistro
def categoriaRegistro(request):
    form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriaData'))
    data = {
        'form': form
    }
    return render(request, 'gestorProductos/categoriaRegistro.html', data)
    
#vista productoRegistro
#vista antigua
#def productoRegistro(request):
#    form = ProductoForm()
#    if request.method == 'POST':
#        form = ProductoForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('productoData'))
#    data = {
#        'form': form        
#    }
#    return render(request, 'gestorProductos/productoRegistro.html', data)
    
#vista nueva
def productoRegistro(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)  # No guardar aún
            producto.user_id = request.user  # Asignar el usuario autenticado
            producto.save()  # Guardar con el usuario
            return HttpResponseRedirect(reverse('productoData'))
    else:
        form = ProductoForm()

    return render(request, 'gestorProductos/productoRegistro.html', {'form': form})

#eliminar categoría
def categoriaEliminar(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return HttpResponseRedirect(reverse('categoriaData'))

#eliminar producto
def productoEliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()    
    return HttpResponseRedirect(reverse('productoData'))

#editar categoría
def categoriaEditar(request,id):
    categoria = Categoria.objects.get(id=id)
    form = CategoriaForm(instance=categoria)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categoriaData'))
    data = {
        'form': form
    }
    return render(request, 'gestorProductos/categoriaRegistro.html', data)
    
#editar producto
def productoEditar(request,id):
    producto = Producto.objects.get(id=id)
    form = ProductoForm(instance=producto)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('productoData'))
        
    data = {'form': form}
    return render(request, 'gestorProductos/productoRegistro.html', data)
