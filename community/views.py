from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Audience, Doctor
from .serializers import AudienceSerializer, DoctorSerializer, UpdateDoctorSerializer


class AudienceViewSet(ModelViewSet):
    http_method_names = ["get", "put"]
    queryset = Audience.objects.all().select_related("user")
    serializer_class = AudienceSerializer

    @action(detail=False, methods=["get", "put"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        audience = get_object_or_404(Audience, user=user)

        if request.method == "GET":
            serializer = self.get_serializer(audience)
            return Response(serializer.data)

        elif request.method == "PUT":
            serializer = self.get_serializer(audience, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all().select_related("user")
    serializer_class = DoctorSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

    @action(detail=False, methods=["get", "put"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        doctor = get_object_or_404(Doctor, user=user)

        if request.method == "GET":
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)

        elif request.method == "PUT":
            serializer = UpdateDoctorSerializer(
                doctor, data=request.data, context={"user": request.user}
            )
            serializer.is_valid(raise_exception=True)
            doctor = serializer.save()
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
