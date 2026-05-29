# moto/models/__init__.py

from .cliente import Cliente
from .vendedor import Vendedor
from .moto import Moto
from .venta import Venta
from .detalle_venta import DetalleVenta

__all__ = [
    'Cliente',
    'Vendedor',
    'Moto',
    'Venta',
    'DetalleVenta',
]