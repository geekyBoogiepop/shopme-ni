from django.contrib.auth.models import User
from django.db import models

from producto.models import Producto

class Conversacion(models.Model):
    producto = models.ForeignKey(Producto, related_name="conversaciones", on_delete=models.CASCADE)
    miembros = models.ManyToManyField(User, related_name="conversaciones")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-modified_at", )

class MensajesConversacion(models.Model):
    conversacion = models.ForeignKey(Conversacion, related_name="mensajes", on_delete=models.CASCADE)
    contenido = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="mensajes_creados", on_delete=models.CASCADE)