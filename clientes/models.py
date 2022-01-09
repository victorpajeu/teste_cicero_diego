from django.db import models

from enderecos.models import Endereco

JURIDICO = 'juridico'
FISICO = 'fisico'
ESPECIAL = 'especial'


TIPOS_CLIENTES = (
    (JURIDICO, 'Jurídico'),
    (FISICO, 'Físico'),
    (ESPECIAL, 'Especial'),
)


class Cliente(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de atualização', auto_now=True)
    nome = models.CharField(max_length=128, null=False, unique=True)
    data_remocao = models.DateTimeField('Data de atualização', auto_now=True)
    tipo = models.CharField(max_length=28, choices=TIPOS_CLIENTES)


class Ponto(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de atualização', auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=False)
    data_remocao = models.DateTimeField(auto_now=True)
