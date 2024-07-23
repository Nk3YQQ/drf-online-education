from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """ Проверка на модератора """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Модератор').exists()


class IsOwner(permissions.BasePermission):
    """ Проверка на владельца """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsUser(permissions.BasePermission):
    """ Проверка на пользователя """

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email
