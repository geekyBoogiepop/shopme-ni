from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import FormularioNuevoProducto
from .models import Producto

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