from django.db import models

class Depoimentos(models.Model):
    imagem_depoimento = models.ImageField()
    nome_depoimento = models.CharField(max_length=100)
    texto_depoimento = models.TextField()

