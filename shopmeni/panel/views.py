from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from producto.models import Producto

@login_required
def index(request):
    productos = Producto.objects.filter(created_by=request.user)

    context = {
        "productos": productos
    }
    return render(request, "panel/index.html", context)