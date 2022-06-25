from django.shortcuts import render
from .models import Depoimentos


def index(request):
    depoimentos = Depoimentos.objects.all()

    dados = {
        "dados_depoimentos": depoimentos
    }

    return render(request,'index.html', dados)
    
def sobre(request):
    return render(request, 'sobre.html')