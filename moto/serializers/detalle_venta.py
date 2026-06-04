from rest_framework import serializers
from moto.models import DetalleVenta


class DetalleVentaSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()
    moto_nombre = serializers.SerializerMethodField()

    class Meta:
        model = DetalleVenta
        fields = [
            'id',
            'venta',
            'moto',
            'cantidad',
            'precio_unitario',
            'subtotal',
            'moto_nombre',
        ]

    def get_subtotal(self, obj):
        return obj.cantidad * obj.precio_unitario

    def get_moto_nombre(self, obj):
        return f"{obj.moto.marca} {obj.moto.modelo}"

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor a 0.")
        return value

    def validate_precio_unitario(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio unitario debe ser mayor a 0.")
        return value

    def validate(self, data):
        moto = data.get('moto')
        cantidad = data.get('cantidad')

        if moto and cantidad and cantidad > moto.stock:
            raise serializers.ValidationError({
                "cantidad": "La cantidad no puede ser mayor al stock disponible."
            })

        return data