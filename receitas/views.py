from cgitb import reset

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):  # pagina inicial

    return render(request, 'home.html')     # paginas cerregadas na pasta templetes


def contato(request):  # pagina contato

    return render(request, 'contato.html')


def sobre(request):  # pagina sobre

    return render(request,'sobre.html')


def teste(request):  # pagina teste

    return render(request,'teste.html')
