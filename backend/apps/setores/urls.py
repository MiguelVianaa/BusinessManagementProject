from django.urls import path, include
from apps.setores.views import index, show, store, edit, update, destroy
from rest_framework import routers
from .views import SetorViewSet

router = routers.DefaultRouter()
router.register(r'setores', SetorViewSet)

app_name = 'setores'

urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
    path('store', store, name='store'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('destroy/<int:id>/', destroy, name='destroy'),


]