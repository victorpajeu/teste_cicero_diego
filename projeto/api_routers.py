from rest_framework import routers

# viewsets
from clientes.api.viewsets import ClienteViewSet
from clientes.api.viewsets import PontoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from contrato.api.viewsets import ContratoViewSet

router = routers.DefaultRouter()

# clientes routes
router.register('clientes', ClienteViewSet)
router.register('cliente', ClienteViewSet)

router.register('pontos', PontoViewSet)
router.register('ponto', PontoViewSet)

router.register('enderecos', EnderecoViewSet)
router.register('endereco', EnderecoViewSet)

router.register('contratos', ContratoViewSet)
router.register('contrato', ContratoViewSet)



default_routers = router.urls