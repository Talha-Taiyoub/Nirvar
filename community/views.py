from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Audience
from .serializers import AudienceSerializer


class AudienceViewSet(ModelViewSet):
    http_method_names = ["get", "patch"]
    queryset = Audience.objects.all().select_related("user")
    serializer_class = AudienceSerializer

    @action(detail=False, methods=["get", "patch"])
    def me(self, request):
        user = request.user
        audience = get_object_or_404(Audience, user=user)

        if request.method == "GET":
            serializer = self.get_serializer(audience)
            return Response(serializer.data)

        elif request.method == "PATCH":
            serializer = self.get_serializer(audience, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
