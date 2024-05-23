from django.urls import include, path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views

router = DefaultRouter()
router.register(
    "personal_stories", views.PersonalStoryViewSet, basename="personal_story"
)

personal_story_router = NestedDefaultRouter(
    router, "personal_stories", lookup="personal_story"
)
personal_story_router.register(
    "images", views.PersonalStoryImageViewSet, basename="personal_story_image"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(personal_story_router.urls)),
]


# router.register("genres", views.GenreViewSet, basename="genre")
# router.register("writers", views.WriterViewSet, basename="writer")
# router.register("books", views.BookViewSet, basename="book")
# router.register("bookitems", views.BookItemViewSetForSeller, basename="book-item")

# book_item_router = NestedDefaultRouter(router, "books", lookup="book")
# book_item_router.register("bookitems", views.BookItemViewSet, basename="book-item")

# feedback_router = NestedDefaultRouter(router, "books", lookup="book")
# feedback_router.register("feedbacks", views.FeedbackViewSet, basename="feedback")


# urlpatterns = [
#     path("", include(router.urls)),
#     path("", include(book_item_router.urls)),
#     path("", include(feedback_router.urls)),
# ]
