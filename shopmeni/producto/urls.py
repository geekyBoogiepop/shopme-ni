from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.productos, name="productos"),
    path("new/", views.nuevo, name="nuevo"),
    path("<int:pk>/", views.detalles, name="detalles"),
    path("<int:pk>/eliminar/", views.eliminar, name="eliminar"),
    path("<int:pk>/editar/", views.editar, name="editar"),
]