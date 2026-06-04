from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from moto.models import Venta
from moto.serializers.venta import VentaSerializer
from moto.permissions import IsStaffOrReadOnly
from moto.pagination import StandardPagination
from moto.filters import VentaFilter


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = VentaFilter

    search_fields = [
        'cliente__nombre',
        'cliente__apellido',
        'cliente__cedula',
        'cliente__correo',
        'vendedor__nombre',
        'vendedor__apellido',
        'vendedor__cedula',
        'vendedor__correo',
        'metodo_pago',
    ]

    ordering_fields = [
        'id',
        'fecha_venta',
        'total',
        'metodo_pago',
        'cliente',
        'vendedor',
    ]

    ordering = ['id']

    @action(detail=False, methods=['get'])
    def stats(self, request):
        ventas = Venta.objects.all()

        return Response({
            'total': ventas.count(),
            'detail': [
                {
                    'id': v.id,
                    'cliente': v.cliente.id if v.cliente else None,
                    'cliente_nombre': f"{v.cliente.nombre} {v.cliente.apellido}" if v.cliente else None,
                    'vendedor': v.vendedor.id if v.vendedor else None,
                    'vendedor_nombre': f"{v.vendedor.nombre} {v.vendedor.apellido}" if v.vendedor else None,
                    'fecha_venta': v.fecha_venta,
                    'metodo_pago': v.metodo_pago,
                    'total': v.total,
                }
                for v in ventas
            ]
        })