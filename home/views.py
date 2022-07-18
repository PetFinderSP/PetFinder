from django.shortcuts import render
from .models import Depoimentos
import random


def index(request):
    depoimentos = Depoimentos.objects.all()

    depoimentos = random.sample(list(depoimentos), 3,)

    dados = {
        "dados_depoimentos": depoimentos
    }

    return render(request,'index.html', dados)
    
def sobre(request):
    return render(request, 'sobre.html')