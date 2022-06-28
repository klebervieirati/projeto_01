from django.urls import path
from receitas.views import contato, home, sobre,teste   # FUNÇÕES E SEUS CAMINHOS(path)

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
    path('teste/', teste ),
]