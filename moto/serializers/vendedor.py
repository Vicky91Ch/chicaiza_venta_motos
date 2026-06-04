from rest_framework import serializers
from moto.models import Vendedor


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = [
            'id',
            'nombre',
            'apellido',
            'cedula',
            'telefono',
            'correo',
        ]

    def validate_cedula(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("La cédula debe tener 10 dígitos.")
        return value