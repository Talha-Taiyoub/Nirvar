from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    raw_content = serializers.CharField(write_only=True)
    content = serializers.CharField(read_only=True)

    class Meta:
        model = Testimonial
        fields = ["id", "user", "title", "raw_content", "content", "created_at"]
