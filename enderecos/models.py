from django.db import models
from django.utils.timezone import now


class Endereco(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de atualização', auto_now=True)
    logradouro = models.CharField(max_length=128, null=False)
    bairro = models.CharField(max_length=128, null=False)
    numero = models.SmallIntegerField(null=False)
    data_remocao = models.DateTimeField(auto_now=True)
