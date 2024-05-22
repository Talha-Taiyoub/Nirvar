from django.db.models import Avg, Count, Min, Sum
from rest_framework.viewsets import ModelViewSet

from .models import Answer, Like, Question, Testimonial
from .serializers import TestimonialSerializer

# Create your views here.


class TestimonialViewSet(ModelViewSet):
    queryset = Testimonial.objects.all().select_related("user")
    serializer_class = TestimonialSerializer
