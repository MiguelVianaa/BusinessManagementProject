from django.shortcuts import render
from .models import Empresa

# Create your views here.
def index(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/index.html', {
        'empresas': empresas
    })
def show(request):
    return render(request, 'empresas/form.html')

def store(request):
    return render(request, 'empresas/form.html')