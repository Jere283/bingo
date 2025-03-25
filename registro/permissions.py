# permissions.py

from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = 'You need to be an admin to perfom this action'

    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user.is_superuser == True and request.user.is_staff == True
