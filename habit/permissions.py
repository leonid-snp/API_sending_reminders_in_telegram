from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """
    Проверяем принадлежит ли объект пользователю.
    """
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False
