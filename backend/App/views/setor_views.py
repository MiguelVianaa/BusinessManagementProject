from rest_framework import viewsets, status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from django.db import transaction

from ..models import Setor
from ..serializers import SetorSerializer

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.filter(deleted_at__isnull=True)
    serializer_class = SetorSerializer

    # GET /api/setores/ → lista com filtros simples
    def list(self, request, *args, **kwargs):
        search = request.GET.get('search', None)

        qs = self.queryset
        if search:
            qs = qs.filter(
                Q(nome__icontains=search) |
                Q(descricao__icontains=search)
            )

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST /api/setores/ → salvar com regras extras
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT/PATCH /api/setores/{id}/ → atualizar com regras extras
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /api/setores/{id}/ → deletar
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)

    # GET /api/setores/datatable/ → endpoint para DataTables
    @action(detail=False, methods=['get'])
    def datatable(self, request):
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        search_value = request.GET.get('search[value]', "")

        setores = self.queryset
        total = setores.count()

        if search_value:
            setores = setores.filter(
                Q(nome__icontains=search_value) |
                Q(descricao__icontains=search_value)
            )

        filtrados = setores.count()

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
        data = self.get_serializer(setores, many=True).data

        return Response({
            'draw': draw,
            'recordsTotal': total,
            'recordsFiltered': filtrados,
            'data': data
        }, status=status.HTTP_200_OK)
