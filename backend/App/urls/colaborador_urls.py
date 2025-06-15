from django.urls import path
from ..views import colaborador_views

app_name = 'colaboradores'

urlpatterns = [
    path('datatable/', colaborador_views.index, name='colaboradores_datatable'),
    path('show/', colaborador_views.show, name='show'),
    path('store', colaborador_views.store, name='store'),
    path('edit/<int:id>/', colaborador_views.edit, name='edit'),
    path('update/<int:id>/', colaborador_views.update, name='update'),
    path('destroy/<int:id>/', colaborador_views.destroy, name='destroy')
]