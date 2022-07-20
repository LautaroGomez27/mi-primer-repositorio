from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola mundo")

def saludar_a(request, nombre):
    return HttpResponse(f"hola com estas{nombre}")

def saludar_a_alguien(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]

    return render(request, "Mi_App/index.html", context)

