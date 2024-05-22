from rest_framework import serializers

from .models import Personal_Story


class PersonalStorySerializer(serializers.ModelSerializer):
    raw_content = serializers.CharField(write_only=True)
    content = serializers.CharField(read_only=True)

    class Meta:
        model = Personal_Story
        fields = ["id", "user", "title", "raw_content", "content", "created_at"]

    def to_representation(self, personal_story):
        representation = super().to_representation(personal_story)
        representation["user"] = personal_story.user.username
        return representation


class UpdatePersonalStorySerializer(serializers.ModelSerializer):
    raw_content = serializers.CharField(write_only=True)
    content = serializers.CharField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Personal_Story
        fields = ["id", "user", "title", "raw_content", "content", "created_at"]

    def save(self, **kwargs):
        personal_story = self.instance
        user = self.context["user"]

        if personal_story.user.id == user.id:
            personal_story.title = self.validated_data["title"]
            personal_story.raw_content = self.validated_data["raw_content"]
            personal_story.save()
            self.instance = personal_story
            return self.instance
        else:
            raise serializers.ValidationError(
                {"error": "This is not your story. You can't update or delete this"}
            )
