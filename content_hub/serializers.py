from rest_framework import serializers

from core.models import User

from .models import Personal_Story, PersonalStoryImage


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class PersonalStoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalStoryImage
        fields = ["id", "image"]

    def create(self, validated_data):
        personal_story_id = self.context["personal_story_id"]
        personal_story = Personal_Story.objects.get(id=personal_story_id)
        return PersonalStoryImage.objects.create(
            personal_story=personal_story, **validated_data
        )


class PersonalStorySerializer(serializers.ModelSerializer):
    images = PersonalStoryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Personal_Story
        fields = [
            "id",
            "user",
            "title",
            "content",
            "raw_content",
            "images",
            "created_at",
        ]

    user = SimpleUserSerializer(read_only=True)
    content = serializers.CharField(read_only=True)
    raw_content = serializers.CharField(write_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    def save(self, **kwargs):
        user = self.context["user"]
        self.instance = Personal_Story.objects.create(**self.validated_data, user=user)
        return self.instance


class UpdatePersonalStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Story
        fields = ["title", "raw_content"]

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
