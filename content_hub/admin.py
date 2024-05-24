from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "raw_content", "created_at"]


@admin.register(models.Personal_Story)
class PersonalStoryAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "title", "raw_content", "created_at"]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "content", "created_at"]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "content", "user", "verified", "created_at"]
    list_select_related = ["question"]


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "target_audience",
        "user",
        "created_at",
    ]


@admin.register(models.SymptomsDiary)
class SymptomsDiaryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "start_date",
        "finish_date",
        "pain_intensity",
        "other_symptoms",
    ]
