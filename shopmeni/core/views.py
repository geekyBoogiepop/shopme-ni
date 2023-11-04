from django.shortcuts import render

from producto.models import Categoria, Producto

def index(request):
    productos = Producto.objects.filter(is_sold=False)[:6]
    categorias = Categoria.objects.all()
    
    context = {
        "productos": productos,
        "categorias": categorias
    }

    return render(request, "core/index.html", context)

def contacto(request):
    return render(request, "core/contact.html")