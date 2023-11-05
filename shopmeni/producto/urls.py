from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("new/", views.nuevo, name="nuevo"),
    path("<int:pk>/", views.detalles, name="detalles"),
]