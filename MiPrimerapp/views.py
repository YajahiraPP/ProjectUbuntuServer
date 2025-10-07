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

def about(request):
    return render(request, "MiPrimerapp/about.html")

def index2(request):
    return render(request, "MiPrimerapp/index2.html")

def tasks_index(request):
    return render(request, "MiPrimerapp/tasks_index.html", {"tasks": tasks})

def tasks_add(request):
    if request.method == "POST":
        new_task = request.POST.get("task")
        if new_task:
            tasks.append(new_task)
    return render(request, "MiPrimerapp/tasks_add.html")

def tasks_admin_list(request):
    return render(request, "MiPrimerapp/tasks_admin_list.html", {"tasks": tasks})
