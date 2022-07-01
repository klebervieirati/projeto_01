from cgitb import reset
from django.shortcuts import render

# (render) USADO PARA CARREGAR AS PAGINAS HTML USA DOS PARAMETROS(request e nome do arquivo html)

# Create your views here.


def home(request):  # pagina inicial

    # paginas cerregadas na pasta templates
    return render(request, 'home/home.html')     

def contato(request):  # pagina contato

    return render(request, 'contatos/contato.html')

def sobre(request):  # pagina sobre

    return render(request, 'sobre/sobre.html')

def teste(request):  # pagina teste

    return render(request, 'teste.html')
