from rest_framework import serializers
from moto.models import Moto


class MotoSerializer(serializers.ModelSerializer):
    cilindraje = serializers.IntegerField(required=False, default=150)
    estado = serializers.CharField(required=False, default="disponible")

    class Meta:
        model = Moto
        fields = [
            'id',
            'marca',
            'modelo',
            'anio',
            'color',
            'precio',
            'stock',
            'cilindraje',
            'estado',
        ]

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value

    def validate_anio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El año debe ser mayor a 0.")
        return value

    def validate_cilindraje(self, value):
        if value <= 0:
            raise serializers.ValidationError("El cilindraje debe ser mayor a 0.")
        return value