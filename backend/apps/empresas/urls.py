from django.urls import path
from apps.empresas.views import index, show, store, edit, update, destroy

app_name = 'empresas'

urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
    path('store', store, name='store'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('destroy/<int:id>/', destroy, name='destroy')
]