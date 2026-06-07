from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import ProtectedError

from moto.models import Moto
from moto.serializers.moto import MotoSerializer
from moto.permissions import IsStaffOrReadOnly
from moto.pagination import StandardPagination
from moto.filters import MotoFilter


class MotoViewSet(viewsets.ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = StandardPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MotoFilter

    search_fields = [
        'marca',
        'modelo',
        'color',
        'estado',
    ]

    ordering_fields = [
        'id',
        'marca',
        'modelo',
        'anio',
        'precio',
        'stock',
        'cilindraje',
        'estado',
    ]

    ordering = ['id']

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(
                {"error": "No se puede eliminar esta moto porque tiene ventas asociadas."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=['get'])
    def stats(self, request):
        motos = Moto.objects.all()

        return Response({
            'total': motos.count(),
            'detail': [
                {
                    'id': m.id,
                    'marca': m.marca,
                    'modelo': m.modelo,
                    'anio': m.anio,
                    'color': m.color,
                    'precio': m.precio,
                    'stock': m.stock,
                    'cilindraje': m.cilindraje,
                    'estado': m.estado,
                }
                for m in motos
            ]
        })