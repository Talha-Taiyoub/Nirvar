from django.db.models import Avg, Count, Min, Sum
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.permissions import IsDoctor

from .models import (
    Answer,
    Like,
    Personal_Story,
    PersonalStoryImage,
    Question,
    Testimonial,
)
from .serializers import (
    AnswerSerializer,
    LikeSerializer,
    PersonalStoryImageSerializer,
    PersonalStorySerializer,
    QuestionSerializer,
    TestimonialSerializer,
    UpdateAnswerSerializer,
    UpdatePersonalStorySerializer,
    UpdateQuestionSerializer,
    UpdateTestimonialSerializer,
    VerifyAnswerSerializer,
)


# Create your views here.
class TestimonialViewSet(ModelViewSet):
    http_method_names = ["get", "put", "post", "delete"]
    queryset = Testimonial.objects.all().select_related("user").order_by("-created_at")
    serializer_class = TestimonialSerializer

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UpdateTestimonialSerializer
        else:
            return TestimonialSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

    def get_permissions(self):
        if self.request.method in ["PUT", "POST", "DELETE"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UpdateTestimonialSerializer(
            instance, data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        testimonial = serializer.save()
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user.id == instance.user.id:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                data={"error": "This is not your testimonial. You can't delete this"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    # @action(detail=False, methods=["get"], url_path=r"user/(?P<user_id>\d+)")
    # def testimonial_by_user(self, request, user_id=None):
    #     queryset = Testimonial.objects.filter(user_id=user_id).select_related("user")
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        queryset = (
            Testimonial.objects.filter(user_id=user.id)
            .select_related("user")
            .order_by("-created_at")
        )
        serializer = TestimonialSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonalStoryViewSet(ModelViewSet):
    http_method_names = ["get", "put", "post", "delete"]
    queryset = (
        Personal_Story.objects.all()
        .select_related("user")
        .prefetch_related("images")
        .order_by("-created_at")
    )
    serializer_class = PersonalStorySerializer

    def get_serializer_class(self):

        if self.request.method == "PUT":
            return UpdatePersonalStorySerializer
        else:
            return PersonalStorySerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

    def get_permissions(self):
        if self.request.method in ["PUT", "POST", "DELETE"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UpdatePersonalStorySerializer(
            instance, data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        personal_story = serializer.save()
        serializer = PersonalStorySerializer(personal_story)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user.id == instance.user.id:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                data={"error": "This is not your story. You can't delete this"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

    @action(detail=False, methods=["get"], url_path=r"user/(?P<user_id>\d+)")
    def personal_story_by_user(self, request, user_id=None):
        queryset = (
            Personal_Story.objects.filter(user_id=user_id)
            .select_related("user")
            .prefetch_related("images")
            .order_by("-created_at")
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        queryset = (
            Personal_Story.objects.filter(user_id=user.id)
            .select_related("user")
            .prefetch_related("images")
            .order_by("-created_at")
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PersonalStoryImageViewSet(ModelViewSet):
    serializer_class = PersonalStoryImageSerializer

    def get_queryset(self):
        return PersonalStoryImage.objects.filter(
            personal_story__id=self.kwargs["personal_story_pk"]
        )

    def get_serializer_context(self):
        return {"personal_story_id": self.kwargs["personal_story_pk"]}


class QuestionViewSet(ModelViewSet):
    http_method_names = ["get", "put", "post", "delete"]
    queryset = Question.objects.all().select_related("user").order_by("-created_at")

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UpdateQuestionSerializer
        else:
            return QuestionSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

    def get_permissions(self):
        if self.request.method in ["PUT", "POST", "DELETE"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        queryset = (
            Question.objects.filter(user_id=user.id)
            .select_related("user")
            .order_by("-created_at")
        )
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerViewSet(ModelViewSet):
    http_method_names = ["get", "put", "post", "delete"]

    def get_queryset(self):
        return (
            Answer.objects.filter(question__id=self.kwargs["question_pk"])
            .annotate(like_count=Count("like"))
            .select_related("user")
            .select_related("question")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return UpdateAnswerSerializer
        else:
            return AnswerSerializer

    def get_serializer_context(self):
        return {"user": self.request.user, "question_id": self.kwargs["question_pk"]}

    def get_permissions(self):
        if self.request.method in ["PUT", "POST", "DELETE"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    @action(detail=True, methods=["put"], permission_classes=[IsDoctor])
    def verify(self, request, *args, **kwargs):
        answer = get_object_or_404(
            Answer, pk=self.kwargs["pk"], question_id=self.kwargs["question_pk"]
        )
        serializer = VerifyAnswerSerializer(answer, data=request.data)
        serializer.is_valid(raise_exception=True)
        answer = serializer.save()
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)


class LikeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["post", "delete"]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        answer_id = self.kwargs.get("answer_pk")
        try:
            answer = Answer.objects.get(id=answer_id)
        except Answer.DoesNotExist:
            raise ValidationError({"detail": "Answer not found."})

        # Check if the like already exists
        user = request.user
        if Like.objects.filter(user=user, answer=answer).exists():
            raise ValidationError({"detail": "You have already liked this answer."})

        like = Like(user=user, answer=answer)
        like.save()

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
