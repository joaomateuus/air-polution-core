from ast import List
from rest_framework import permissions

# endpoint: account/users/
# - Everyone can create a regular user account
# - Only authenticated users or admins can list
# - Only object owner or admin can Update or Delete
class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        is_admin: bool = request.user.is_superuser \
            or request.user.is_staff
        
        update_methods: List[str] \
            = request.method in ['PUT', 'PATCH', 'DELETE']

        if request.method == 'POST':
            return True

        if request.method == 'GET':
            return request.user.is_authenticated
        
        if update_methods and request.user.is_authenticated:
           return request.user.id == int(view.kwargs['pk']) or is_admin
        
        return False
    