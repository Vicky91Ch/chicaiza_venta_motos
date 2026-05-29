from django.db import models
from .venta import Venta
from .moto import Moto


class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='detalles'
    )
    moto = models.ForeignKey(
        Moto,
        on_delete=models.PROTECT,
        related_name='detalles_venta'
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.precio_unitario * self.cantidad

    def __str__(self):
        return f"{self.cantidad}x {self.moto} - Venta #{self.venta.id}"