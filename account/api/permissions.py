from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from utilities.logger import Logger


class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-authenticated Users only
    """
    message = "You are already authenticated, please log-out"

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.is_employee:
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.is_employee:
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.is_admin:
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False

    def has_object_permission(self, request, view, obj):
        try:
            if request.user.is_admin:
                return True
        except AttributeError:
            Logger.info("an anonymous user is trying to access the endpoint")

        return False


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
