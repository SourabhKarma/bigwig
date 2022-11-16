from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.task_role == request.user:
            return True

        if request.user.is_staff and request.method not in self.edit_methods:
            return True

        return False


class IsobjectUser(permissions.BasePermission):
    """
    Allows access only to object users.
    """

    def has_permission(self, request, view):
        return bool(request.user)



class IsOwner(permissions.BasePermission):
    message = 'YES'

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        # I need to filter who can only edit book in this part but
        # obj.authors when print is none
        # if request.user in obj.task_role :
        #     return True

        # return False
        return obj.task_role == request.user
