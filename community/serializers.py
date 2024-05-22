from rest_framework import serializers

from core.models import User

from .models import Audience, Doctor


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = ["user", "gender", "age", "education", "address", "created_at"]

    user = SimpleUserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "user",
            "gender",
            "age",
            "address",
            "medical_college",
            "degree",
            "linkedIn",
            "year_of_passing",
            "verified",
            "created_at",
        ]

    user = SimpleUserSerializer(read_only=True)
    verified = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
