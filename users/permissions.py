from rest_framework import permissions


class IsActivePermission(permissions.BasePermission):
    """Проверка активных пользователей"""
    message = "User must be active"

    def has_permission(self, request, view):
        if request.user.is_active:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
