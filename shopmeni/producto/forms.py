from django import forms

from .models import Producto

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class FormularioNuevoProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            "categoria",
            "name",
            "description",
            "price",
            "image",
        )
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "price": "Precio",
            "image": "Imagen"
        }

        widgets = {
            "categoria": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }

class FormularioEditarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            "categoria",
            "name",
            "description",
            "price",
            "image",
            "is_sold",
        )
        labels = {
            "name": "Nombre",
            "description": "Descripción",
            "price": "Precio",
            "image": "Imagen",
            "is_sold": "Vendido"
        }

        widgets = {
            "categoria": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.NumberInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }
