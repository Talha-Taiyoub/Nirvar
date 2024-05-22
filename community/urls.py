from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register("audience", views.AudienceViewSet, basename="audience")
router.register("doctors", views.DoctorViewSet, basename="doctor")

urlpatterns = [
    path("", include(router.urls)),
]
