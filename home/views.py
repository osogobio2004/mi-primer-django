from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def multimedia(request):
    return render(request, 'home/multimedia.html')

def proyectos(request):
    return render(request, 'home/proyectos.html')