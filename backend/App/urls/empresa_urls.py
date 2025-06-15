from django.urls import path
from ..views import empresa_views

app_name = 'empresas'

urlpatterns = [
    path('datatable/', empresa_views.datatable, name='empresas_datatable'),
    path('show/', empresa_views.show, name='show'),
    path('store', empresa_views.store, name='store'),
    path('edit/<int:id>/', empresa_views.edit, name='edit'),
    path('update/<int:id>/', empresa_views.update, name='update'),
    path('destroy/<int:id>/', empresa_views.destroy, name='destroy')
]