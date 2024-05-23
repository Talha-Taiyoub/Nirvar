from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register("testimonials", views.TestimonialViewSet, basename="testimonial")

router.register(
    "personal_stories", views.PersonalStoryViewSet, basename="personal_story"
)
personal_story_image_router = NestedDefaultRouter(
    router, "personal_stories", lookup="personal_story"
)
personal_story_image_router.register(
    "images", views.PersonalStoryImageViewSet, basename="personal_story_image"
)


router.register("questions", views.QuestionViewSet, basename="question")
answer_router = NestedDefaultRouter(router, "questions", lookup="question")
answer_router.register("answers", views.AnswerViewSet, basename="answer")
like_router = NestedDefaultRouter(answer_router, "answers", lookup="answer")
like_router.register("likes", views.LikeViewSet, basename="like")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(personal_story_image_router.urls)),
    path("", include(answer_router.urls)),
    path("", include(like_router.urls)),
]
