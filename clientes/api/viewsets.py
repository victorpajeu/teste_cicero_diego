from rest_framework import viewsets

# models
from clientes.models import Cliente
from clientes.models import Ponto

# serializers
from clientes.api.serializers import ClienteSerialize
from clientes.api.serializers import PontoSerialize


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerialize


class PontoViewSet(viewsets.ModelViewSet):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerialize
