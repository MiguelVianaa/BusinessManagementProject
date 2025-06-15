from django.urls import path, include
from rest_framework import routers
from ..views import SetorViewSet

router = routers.DefaultRouter()
router.register(r'setores', SetorViewSet, basename='setor-api')

urlpatterns = [
    path('api/setores/', include('App.urls.setor_urls')),
    path('api/', include(router.urls)),
]