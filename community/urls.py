from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register("audience", views.AudienceViewSet, basename="audience")

urlpatterns = [
    path("", include(router.urls)),
]
