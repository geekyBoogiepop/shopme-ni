from django.urls import path

from . import views

app_name = "mensajes"

urlpatterns = [
    path("", views.conversaciones, name="conversaciones"),
    path("nuevo/<int:producto_pk>/", views.nueva_conversacion, name="nuevo"),
    path("<int:pk>/", views.detalles, name="detalles"),
]