from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("<int:pk>/", views.detalles, name="detalles"),
]