from rest_framework import viewsets

# models
from enderecos.models import Endereco

# serializers
from enderecos.api.serializers import EnderecoSerialize


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerialize
