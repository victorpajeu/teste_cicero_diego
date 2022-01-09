from rest_framework import serializers

# models
from enderecos.models import Endereco


class EnderecoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('logradouro', 'bairro', 'numero')
