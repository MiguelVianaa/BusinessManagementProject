from django.urls import path
from ..views import cargo_views

app_name = 'cargos'

urlpatterns = [
    path('datatable/', cargo_views.datatable, name='cargos_datatable'),
    path('show/', cargo_views.show, name='show'),
    path('store', cargo_views.store, name='store'),
    path('edit/<int:id>/', cargo_views.edit, name='edit'),
    path('update/<int:id>/', cargo_views.update, name='update'),
    path('destroy/<int:id>/', cargo_views.destroy, name='destroy')
]