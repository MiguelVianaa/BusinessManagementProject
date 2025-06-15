from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
from ..serializers import EmpresaSerializer
from ..forms import EmpresaForm
from ..models import Empresa

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

def datatable(request):
    return render(request, 'empresas/index.html', {
        'empresas': Empresa.objects.filter(deleted_at__isnull=True)
    })

def show(request):
    return render(request, 'empresas/form.html',{
        'form': EmpresaForm(),
        'form_action': reverse('empresas:store'),
    })


def store(request):
    if request.method  == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('empresas:index')
        else:
            return render(request, 'empresas/form.html', {
                'form': form
            })

    return redirect('empresas:index')


def edit(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    form = EmpresaForm(instance=empresa)

    return render(request, 'empresas/form.html', {
        'form': form,
        'form_action': reverse('empresas:update', args=[id]),
        'empresa': empresa
    })


def update(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method  == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('empresas:index')
        else:
            return render(request, 'empresas/form.html', {
                'form': form,
                'empresa': empresa
            })

    return redirect('empresas:index')


def destroy(request, id):
    empresa = get_object_or_404(Empresa, id=id)

    if request.method == 'POST' and empresa:
        empresa.delete()

    return redirect('empresas:index')
