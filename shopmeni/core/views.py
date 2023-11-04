from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def contacto(request):
    return render(request, "core/contact.html")