import uuid

from django.db import models

from clientes.models import Ponto

EM_VIGOR = 'Em vigor'
DESATIVADO_TEMPORARIO = 'Desativado Temporario'
CANCELADO = 'Cancelado'


CONTRATO_ESTADO = (
    (EM_VIGOR, 'Em vigor'),
    (DESATIVADO_TEMPORARIO, 'Desativado Temporario'),
    (CANCELADO, 'Cancelado'),
)


class Contrato(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de atualização', auto_now=True)
    ponto = models.OneToOneField(Ponto, on_delete=models.CASCADE, null=False)
    estado = models.CharField(max_length=28, choices=CONTRATO_ESTADO)
    data_remocao = models.DateTimeField(auto_now=True)


class ContratoEvento(models.Model):
    data_criacao = models.DateTimeField('Data de criação', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de atualização', auto_now=True)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, null=False)
    estado_anterior = models.CharField(max_length=28, choices=CONTRATO_ESTADO)
    estado_posterior = models.CharField(max_length=28, choices=CONTRATO_ESTADO)
