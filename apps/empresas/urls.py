
from django.urls import path
from apps.empresas.views import index, show, store, edit, update

urlpatterns = [
    path('empresas', index, name='empresas'),
    path('empresas/cadastro/', show, name='cadastro'),
    path('empresas/store', store, name='store'),
    path('empresas/edit/<int:id>/', edit, name='editar'),
    path('empresas/update/<int:id>/', update, name='update')
]