from rest_framework import serializers
from moto.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre',
            'apellido',
            'cedula',
            'telefono',
            'correo',
            'direccion',
        ]

    def validate_cedula(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("La cédula debe tener 10 dígitos.")
        return value