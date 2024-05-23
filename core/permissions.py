from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False

        # Check if the user has a doctor attribute and if the doctor is verified
        return hasattr(request.user, "doctor") and request.user.doctor.verified
