from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)


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
    year_of_passing = serializers.DateField(
        format="%d-%m-%Y", input_formats=["%d-%m-%Y", "%Y-%m-%d"]
    )
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    def save(self, **kwargs):
        user = self.context["user"]

        if Doctor.objects.filter(user=user).exists():
            doctor = Doctor.objects.get(user=user)
            if doctor.verified:
                raise ValidationError("You are already registered as a doctor.")
            else:
                raise ValidationError("You've already applied, wait for approvement.")

        self.instance = Doctor.objects.create(user=user, **self.validated_data)
        return self.instance


class UpdateDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "gender",
            "age",
            "address",
            "medical_college",
            "degree",
            "linkedIn",
            "year_of_passing",
        ]

    year_of_passing = serializers.DateField(
        format="%d-%m-%Y", input_formats=["%d-%m-%Y", "%Y-%m-%d"]
    )

    def save(self, **kwargs):
        doctor = self.instance
        user = self.context["user"]

        if doctor.user.id == user.id:
            doctor.gender = self.validated_data["gender"]
            doctor.age = self.validated_data["age"]
            doctor.address = self.validated_data["address"]
            doctor.medical_college = self.validated_data["medical_college"]
            doctor.degree = self.validated_data["degree"]
            doctor.linkedIn = self.validated_data["linkedIn"]
            doctor.year_of_passing = self.validated_data["year_of_passing"]
            doctor.save()
            self.instance = doctor
            return self.instance
        else:
            raise serializers.ValidationError(
                {"error": "This is not your profile. You can't update or delete this"}
            )
