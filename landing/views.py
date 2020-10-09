from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def select(request):
    return render(request, "landing/seleccion.html")

def contacto(request):
    return render(request, "landing/contacto.html")

def desarrollo(request):
    return render(request, "landing/desarrollo.html")

def pricing(request):
    return render(request, "landing/pricing.html")
