from django.urls import path, include
from rest_framework import routers
from ..views import SetorViewSet, EmpresaViewSet, CargoViewSet, ColaboradorViewSet

router = routers.DefaultRouter()
router.register(r'setores', SetorViewSet, basename='setor-api')
router.register(r'empresas', EmpresaViewSet, basename='empresa-api')
router.register(r'cargos', CargoViewSet, basename='cargo-api')
router.register(r'colaboradores', ColaboradorViewSet, basename='colaborador-api')

urlpatterns = [
    path('api/', include(router.urls)),
]