from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from producto.models import Categoria, Producto
from .forms import FormularioRegistro

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

def registrar_usuario(request):
    if request.method == "POST":
        form = FormularioRegistro(request.POST)

        if form.is_valid():
            form.save()

            return redirect("core:login")
    
    form = FormularioRegistro()
    context = {
        "form": form
    }

    return render(request, "core/registro.html", context)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("core:index")