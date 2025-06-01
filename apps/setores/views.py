from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.urls import reverse
from .forms import SetorForm
from .models import Setor

def index(request):
    return render(request, 'setores/index.html', {
        'setores': Setor.objects.filter(deleted_at__isnull=True)
    })


def show(request):
    return render(request, 'setores/form.html',{
        'form': SetorForm(),
        'form_action': reverse('setores:store'),
    })


def store(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)

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
