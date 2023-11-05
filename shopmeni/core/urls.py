from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views
from .forms import FormularioLogin

app_name = "core"

urlpatterns = [
    # / index path
    path("", views.index, name="index"),
    path("contact/", views.contacto, name="contacto"),
    path("registrarse/", views.registrar_usuario, name="registrarse"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=FormularioLogin), name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)