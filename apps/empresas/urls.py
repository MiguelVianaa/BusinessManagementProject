
from django.urls import path
from apps.empresas.views import index

urlpatterns = [
    path('empresas', index, name='empresas'),
]