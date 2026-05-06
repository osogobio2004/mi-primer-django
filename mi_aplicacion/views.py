from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
class Lista(ListView):
    template_name = 'mi_aplicacion/lista.html'
    queryset = ['Elemento 1', 'Elemento 2']
    context_object_name = 'lista'
