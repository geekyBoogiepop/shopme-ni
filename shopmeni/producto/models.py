import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="imagenes_productos", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="productos", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Producto: {self.name} Categoría: {self.categoria.name}"
    
    def save(self, *args, **kwargs):
        try:
            producto_anterior = Producto.objects.get(pk=self.pk)
            imagen_vieja = producto_anterior.image
        except Producto.DoesNotExist:
            imagen_vieja = None

        if self.image and imagen_vieja and self.image.path != imagen_vieja.path:
            print("hola")
            ruta_imagen_vieja = os.path.join(settings.MEDIA_ROOT, imagen_vieja.name)
            if os.path.exists(ruta_imagen_vieja):
                os.remove(ruta_imagen_vieja)

        super(Producto, self).save(*args, **kwargs)