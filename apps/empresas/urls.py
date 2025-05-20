
from django.urls import path
from apps.empresas.views import index, show, store

urlpatterns = [
    path('empresas', index, name='empresas'),
    path('empresas/cadastro/', show, name='cadastro'),
    path('empresas/store', store, name='store'),
]