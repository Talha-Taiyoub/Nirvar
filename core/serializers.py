from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "email", "username", "role"]

    role = serializers.SerializerMethodField(method_name="check_role", read_only=True)

    def check_role(self, user):
        if hasattr(user, "doctor") and user.doctor.verified:
            return "doctor"
        else:
            return "audience"
