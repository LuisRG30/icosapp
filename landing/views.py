from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest

from .models import Message
from .forms import MessageForm

# Create your views here.
messageform = MessageForm()

def index(request):
    return render(request, "landing/index.html", {"messageform": messageform, "nombre": "index"})

def select(request):
    return render(request, "landing/seleccion.html", {"messageform": messageform})

def contacto(request):
    return render(request, "landing/contacto.html", {"messageform": messageform})

def desarrollo(request):
    return render(request, "landing/desarrollo.html", {"messageform": messageform})

def pricing(request):
    return render(request, "landing/pricing.html", {"messageform": messageform})

def business(request):
    return render(request, "landing/business.html")

def web(request):
    return render(request, "landing/web.html")

def mobile(request):
    return render(request, "landing/mobile.html")

def receive_message(request):
    next = request.POST.get('next', '/')
    next = next + "#footer"
    form = MessageForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        return HttpResponseBadRequest("Bad Request")
    return HttpResponseRedirect(next)
