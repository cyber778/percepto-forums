from rest_framework.permissions import IsAdminUser


class IsAdminOrSelf(IsAdminUser):
    """
    Allow access to admin users or the user himself.
    """
    def has_object_permission(self, request, view, obj):
        print('*******************************************************')
        print(obj)
        if request.user and request.user.is_staff:
            return True
        elif (request.user and obj.author == request.user):
            return True
        return False