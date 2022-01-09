from rest_framework import serializers

# models
from contrato.models import Contrato


class ContratoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = ('id', 'ponto')
