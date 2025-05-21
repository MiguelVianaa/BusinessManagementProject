from django.shortcuts import render, redirect
from .models import Empresa
from .forms import EmpresaForm

def index(request):
    return render(request, 'empresas/index.html', {
        'empresas': Empresa.objects.all()
    })

def show(request):
    return render(request, 'empresas/form.html')

def store(request):
    if request.method  == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            empresa = form.save()
            return redirect('empresas')
        else:
            return render(request, 'empresas/form.html', {
                'form': form
            })
    else:
        form = EmpresaForm()
        return render(request, 'empresas/form.html', {
            'form': form
        })