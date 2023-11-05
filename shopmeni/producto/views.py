from django.shortcuts import render, get_object_or_404

from .models import Producto

def detalles(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    context = {
        "producto": producto
    }

    return render(request, "producto/detalles.html", context)
