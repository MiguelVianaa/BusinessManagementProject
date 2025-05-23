from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.urls import reverse
from .models import Empresa
from .forms import EmpresaForm


def index(request):
    return render(request, 'empresas/index.html', {
        'empresas': Empresa.objects.filter(deleted_at__isnull=True)
    })


def show(request):
    return render(request, 'empresas/form.html',{
        'form': EmpresaForm(),
        'form_action': reverse('store'),
    })


def store(request):
    if request.method  == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('empresas')
        else:
            return render(request, 'empresas/form.html', {
                'form': form
            })

    form = EmpresaForm()
    return render(request, 'empresas/form.html', {
        'form': form
    })


def edit(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    form = EmpresaForm(instance=empresa)

    return render(request, 'empresas/form.html', {
        'form': form,
        'form_action': reverse('update', args=[id]),
        'empresa': empresa
    })


def update(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method  == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('empresas')
        else:
            return render(request, 'empresas/form.html', {
                'form': form,
                'empresa': empresa
            })

    form = EmpresaForm(instance=empresa)
    return render(request, 'empresas/form.html', {
        'form': form,
        'empresa': empresa
    })

def destroy(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method == 'POST':
        empresa.delete()
        return redirect('empresas')

    return render(request, 'empresas/destroy.html', {
        'empresa': empresa
    })
