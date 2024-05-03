from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.user.groups.filter(name='Модератор').exists() else False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
