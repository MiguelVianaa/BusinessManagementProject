from django.urls import path
from apps.setores.views import index, show, store, edit, update, destroy

app_name = 'setores'

urlpatterns = [
    path('', index, name='index'),
    path('show/', show, name='show'),
    path('store', store, name='store'),
    path('edit/<int:id>/', edit, name='edit'),
    path('update/<int:id>/', update, name='update'),
    path('destroy/<int:id>/', destroy, name='destroy')
]