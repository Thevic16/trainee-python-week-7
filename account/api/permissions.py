from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-authenticated Users only
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_employee:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_employee:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return False
