# moto/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return bool(request.user and request.user.is_staff)


class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        if hasattr(obj, 'user'):
            return obj.user == request.user

        return False
