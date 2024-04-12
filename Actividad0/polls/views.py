from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo, estas en el indice de encuestas.")

# Create your views here.
