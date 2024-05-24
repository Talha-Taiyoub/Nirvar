import markdown
from django.conf import settings
from django.db import models

USER = settings.AUTH_USER_MODEL

# Create your models here.


class Testimonial(models.Model):
    raw_content = models.TextField()
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def content(self):
        return markdown.markdown(self.raw_content, extensions=["extra"])


class Personal_Story(models.Model):
    title = models.CharField(max_length=255)
    raw_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    @property
    def content(self):
        return markdown.markdown(self.raw_content, extensions=["extra"])


class PersonalStoryImage(models.Model):
    personal_story = models.ForeignKey(
        Personal_Story, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="content_hub/images")


class Question(models.Model):
    content = models.TextField()
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="content_hub/images", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    verified = models.BooleanField(default=False)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["answer", "user"]


class Article(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="content_hub/images", null=True, blank=True)
    target_audience = models.CharField(
        max_length=6,
        choices=[("Male", "Male"), ("Female", "Female"), ("All", "All")],
        default="All",
    )
    minimum_age_required = models.IntegerField()
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class RecommendedByDoctor(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)


class SymptomsDiary(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    pain_intensity = models.TextField()
    other_symptoms = models.TextField()
