from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Q
from ..serializers import CargoSerializer
from ..forms import CargoForm
from ..models import Cargo

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

def datatable(request):
    return


def show(request):
    return


def store(request):
    return


def edit(request, id):
    return


def update(request, id):
    return


def destroy(request, id):
    return

