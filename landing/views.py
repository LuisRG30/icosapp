from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "landing/index.html")

def pricing(request):
    return render(request, "landing/pricing.html")
