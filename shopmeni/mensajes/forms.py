from django import forms

from .models import MensajesConversacion

class FormularioMensajesConversacion(forms.ModelForm):
    class Meta:
        model = MensajesConversacion
        fields = ("contenido",)

        widgets = {
            "contenido": forms.Textarea(attrs={
                "class": "w-full py-4 px-6 rounded-xl border"
            })
        }