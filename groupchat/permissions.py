from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsInGroup(BasePermission):
    message = 'Editing book is restricted to the authors only.'

    # def has_object_permission(self, request, view, obj):
        
    #     if request.method in SAFE_METHODS:
    #         return False
    #     # I need to filter who can only edit book in this part but
    #     # obj.authors when print is none
    #     # if request.user in obj.group_members:
    #     #     print(request.user)
    #     #     print(obj.group_members)
    #     #     return False

    #     # return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user