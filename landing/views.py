from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "landing/index.html",{"nombre": "index"})

def pricing(request):
    return render(request, "landing/pricing.html")

def business(request):
    return render(request, "landing/business.html")

def web(request):
    return render(request, "landing/web.html")

def mobile(request):
    return render(request, "landing/mobile.html")
