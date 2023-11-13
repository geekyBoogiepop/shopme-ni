from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import FormularioNuevoProducto, FormularioEditarProducto
from .models import Producto, Categoria

def productos(request):
    query = request.GET.get("query", "")
    categoria_id = request.GET.get("categoria", 0)

    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(is_sold=False)

    # Filtros
    if query:
        productos = productos.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    
    context = {
        "productos": productos,
        "query": query,
        "categorias": categorias,
        "categoria_id": int(categoria_id),
    }

    return render(request, "producto/productos.html", context)

def detalles(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    productos_relacionados = Producto.objects.filter(categoria=producto.categoria, is_sold=False).exclude(pk=pk)[:3]

    context = {
        "producto": producto,
        "productos_relacionados": productos_relacionados
    }

    return render(request, "producto/detalles.html", context)

@login_required
def nuevo(request):
    if request.method == "POST":
        form = FormularioNuevoProducto(request.POST, request.FILES)

        if form.is_valid():
            producto = form.save(commit=False)
            producto.created_by = request.user
            producto.save()

            return redirect("producto:detalles", pk=producto.id)
        
    form = FormularioNuevoProducto()
    context = {
        "form": form,
        "titulo": "Nuevo producto"
    }

    return render(request, "producto/formulario.html", context)

@login_required
def editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = FormularioEditarProducto(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            producto.save()

            return redirect("producto:detalles", pk=producto.id) # type: ignore
        
    form = FormularioEditarProducto(instance=producto)
    context = {
        "form": form,
        "titulo": "Editar producto"
    }

    return render(request, "producto/formulario.html", context)

@login_required
def eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk, created_by=request.user)
    producto.delete()

    return redirect("panel:index")