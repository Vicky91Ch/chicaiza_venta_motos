# moto/tests/helpers.py

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from moto.models import Cliente, Vendedor, Moto, Venta, DetalleVenta


def create_user(username='user', email=None, password='Pass1234!', **kwargs):
    email = email or f'{username}@test.com'
    return User.objects.create_user(
        username=username,
        email=email,
        password=password,
        **kwargs
    )


def create_staff(username='staff', email=None, password='Admin1234!'):
    email = email or f'{username}@test.com'
    return User.objects.create_user(
        username=username,
        email=email,
        password=password,
        is_staff=True
    )


def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token), str(refresh)


def auth_client(user):
    client = APIClient()
    access, _ = get_tokens(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
    return client


def create_cliente(
    nombre="Juan",
    apellido="Perez",
    cedula="0102030405",
    telefono="0999999999",
    correo=None,
    email=None,
    direccion="Quito",
):
    return Cliente.objects.create(
        nombre=nombre,
        apellido=apellido,
        cedula=cedula,
        telefono=telefono,
        correo=correo or email or "juan.perez@gmail.com",
        direccion=direccion,
    )


def create_vendedor(
    nombre="Carlos",
    apellido="Lopez",
    cedula="0203040506",
    telefono="0988888888",
    correo=None,
    email=None,
    direccion=None,
):
    return Vendedor.objects.create(
        nombre=nombre,
        apellido=apellido,
        cedula=cedula,
        telefono=telefono,
        correo=correo or email or "carlos.lopez@gmail.com",
    )


def create_moto(
    marca="Honda",
    modelo="CBR 500R",
    anio=2023,
    color="Rojo",
    precio=8500.00,
    stock=5,
    cilindraje=500,
    estado="disponible",
    descripcion=None,
):
    return Moto.objects.create(
        marca=marca,
        modelo=modelo,
        anio=anio,
        color=color,
        precio=precio,
        stock=stock,
        cilindraje=cilindraje,
        estado=estado,
    )


def create_venta(
    cliente=None,
    vendedor=None,
    total=3500,
    metodo_pago="efectivo",
):
    if cliente is None:
        cliente = create_cliente()

    if vendedor is None:
        vendedor = create_vendedor()

    return Venta.objects.create(
        cliente=cliente,
        vendedor=vendedor,
        total=total,
        metodo_pago=metodo_pago,
    )


def add_detalle_venta(venta=None, moto=None, cantidad=1, precio_unitario=None):
    if venta is None:
        venta = create_venta()

    if moto is None:
        moto = create_moto()

    if precio_unitario is None:
        precio_unitario = moto.precio

    return DetalleVenta.objects.create(
        venta=venta,
        moto=moto,
        cantidad=cantidad,
        precio_unitario=precio_unitario
    )
