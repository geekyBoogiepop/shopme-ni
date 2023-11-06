from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Conversacion, MensajesConversacion
from producto.models import Producto
from .forms import FormularioMensajesConversacion

@login_required
def nueva_conversacion(request, producto_pk):
    producto = get_object_or_404(Producto, pk=producto_pk)

    # si el producto es creado por el mismo usuario, evita que cree una conversación
    if producto.created_by == request.user:
        return redirect("panel:index")
    
    # obtiene las conversaciones del usuario relacionados con ese producto si existe
    conversaciones = Conversacion.objects.filter(producto=producto).filter(miembros__in=[request.user.id])

    # Si hay conversaciones, redirije al usuario a esa conversación existente
    if conversaciones:
        return redirect("mensajes:detalles", pk=conversaciones.first().id) # type: ignore

    # Si el usuario envía un nuevo mensaje
    if request.method == "POST":
        form = FormularioMensajesConversacion(request.POST)

        # Si el mensaje es válido, crea una conversación del producto con el propietario y el usuario
        if form.is_valid():
            conversacion = Conversacion.objects.create(producto=producto)
            conversacion.miembros.add(request.user)
            conversacion.miembros.add(producto.created_by)

            conversacion.save()

            # Crea los mensajes de la conversación
            mensaje_conversacion: MensajesConversacion = form.save(commit=False)
            mensaje_conversacion.conversacion = conversacion
            mensaje_conversacion.created_by = request.user
            mensaje_conversacion.save()

            return redirect("producto:detalles", pk=producto_pk)
    else:
        form = FormularioMensajesConversacion

    context = {
        "form": form
    }

    return render(request, "mensajes/nuevo.html", context)

@login_required
def conversaciones(request):
    # Obtiene todas las conversaciones en las que participa el usuario
    conversaciones = Conversacion.objects.filter(miembros__in=[request.user.id])

    context = {
        "conversaciones": conversaciones
    }

    return render(request, "mensajes/conversaciones.html", context)

def detalles(request, pk):
    conversacion = Conversacion.objects.filter(miembros__in=[request.user.id]).get(pk=pk)

    if request.method == "POST":
        form = FormularioMensajesConversacion(request.POST)

        if form.is_valid():
            mensaje_conversacion = form.save(commit=False)
            mensaje_conversacion.conversacion = conversacion
            mensaje_conversacion.created_by = request.user
            mensaje_conversacion.save()

            # Actualiza fecha y hora de la última actividad de la conversación
            conversacion.save()

            return redirect("mensajes:detalles", pk=pk)
    else:
        form = FormularioMensajesConversacion()

    context = {
        "conversacion": conversacion,
        "form": form
    }

    return render(request, "mensajes/detalles.html", context)
