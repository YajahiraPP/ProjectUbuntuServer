from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tasks = ["foo", "bar", "baz"]

def index(request):
	return  HttpResponse("Hello, World!")

def suma(request):
    resultado = None  

    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        resultado = num1 + num2  

    return render(request, "MiPrimerapp/suma.html", {"resultado": resultado})


def saludo(request, nombre):
    return render(request, "MiPrimerapp/saludo.html", {"nombre": nombre.capitalize()})

from .models import Task
