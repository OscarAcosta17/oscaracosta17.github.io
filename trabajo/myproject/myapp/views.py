# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("Hola desde mi primera vista en myapp.")
    
