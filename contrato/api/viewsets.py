from rest_framework import viewsets

# models
from contrato.models import Contrato

# serializers
from contrato.api.serializers import ContratoSerialize


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerialize
