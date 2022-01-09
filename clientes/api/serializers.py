from rest_framework import serializers

# models
from clientes.models import Cliente
from clientes.models import Ponto


class ClienteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'tipo')


class PontoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Ponto
        fields = ('cliente', 'enderecos')
