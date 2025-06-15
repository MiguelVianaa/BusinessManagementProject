from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
from ..serializers import SetorSerializer
from ..forms import SetorForm
from ..models import Setor

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


def datatable(request):
    draw = int(request.GET.get('draw', 1))
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', "")

    setores = Setor.objects.filter(deleted_at__isnull=True)
    records_total = setores.count()

    if search_value:
        setores = setores.filter(
            Q(nome__icontains=search_value) |
            Q(descricao__icontains=search_value)
        )
    records_filtered = setores.count()

    order_column_index = request.GET.get('order[0][column]')
    order_dir = request.GET.get('order[0][dir]', 'asc')
    order_column = 'nome'

    if order_column_index is not None:
        try:
            order_column_index = int(order_column_index)
            order_column = request.GET.get(f'columns[{order_column_index}][data]', 'nome')
        except (ValueError, KeyError):
            order_column = 'nome'
        if order_dir == 'desc':
            order_column = f'-{order_column}'

    setores = setores.order_by(order_column)[start:start + length]
    data = [
        {'nome': setor.nome, 'descricao': setor.descricao}
        for setor in setores
    ]

    return JsonResponse({
        'draw': draw,
        'recordsTotal': records_total,
        'recordsFiltered': records_filtered,
        'data': data
    })


def show(request):
    return render(request, 'setores/form.html',{
        'form': '', #TODO: A DEFINIR
        'form_action': reverse('setores:store'),
    })


def store(request):
    if request.method == 'POST':
        form = '' #TODO: A DEFINIR

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('setores:index')
        else:
            return render(request, 'setores/form.html', {
                'form': form
            })

    return redirect('setores:index')


def edit(request, id):
    setor = get_object_or_404(Setor, id=id)

    return render(request, 'setores/form.html', {
        'form': SetorForm(instance=setor),
        'form_action': reverse('setores:update', args=[id]),
        'setor': setor
    })


def update(request, id):
    setor = get_object_or_404(Setor, id=id)

    if request.method == 'POST' and setor:
        form = SetorForm(request.POST, instance=setor)

        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('setores:index')
        else:
            return render(request, 'setores/form.html', {
                'form': form,
                'setor': setor
            })

    return redirect('setores:index')


def destroy(request, id):
    setor = get_object_or_404(Setor, id=id)

    if request.method == 'POST' and setor:
        setor.delete()

    return redirect('setores:index')
