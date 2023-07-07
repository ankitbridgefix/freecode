from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        #print(user.get_all_perimission())
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)