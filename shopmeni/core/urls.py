from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # / index path
    path("", views.index, name="index"),
    path("contact/", views.contacto, name="contacto"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)