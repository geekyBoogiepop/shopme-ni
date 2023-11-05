from django.shortcuts import render, get_object_or_404

from .models import Producto

def detalles(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    productos_relacionados = Producto.objects.filter(categoria=producto.categoria, is_sold=False).exclude(pk=pk)[:3]

    context = {
        "producto": producto,
        "productos_relacionados": productos_relacionados
    }

    return render(request, "producto/detalles.html", context)
