from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from moto.models import Vendedor
from moto.serializers.vendedor import VendedorSerializer
from moto.permissions import IsStaffOrReadOnly
from moto.pagination import StandardPagination
from moto.filters import VendedorFilter


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = VendedorFilter

    search_fields = [
        'nombre',
        'apellido',
        'cedula',
        'correo',
        'telefono',
    ]

    ordering_fields = [
        'id',
        'nombre',
        'apellido',
        'cedula',
        'correo',
        'telefono',
    ]

    ordering = ['id']

    @action(detail=False, methods=['get'])
    def stats(self, request):
        vendedores = Vendedor.objects.annotate(
            total_ventas=Count('ventas_realizadas')
        )

        return Response({
            'total': vendedores.count(),
            'detail': [
                {
                    'id': v.id,
                    'nombre': v.nombre,
                    'apellido': v.apellido,
                    'cedula': v.cedula,
                    'telefono': v.telefono,
                    'correo': v.correo,
                    'total_ventas': v.total_ventas,
                }
                for v in vendedores
            ]
        })