from django.urls import path
from . import views

urlpatterns = [
    # / index path
    path("", views.index, name="index"),
]