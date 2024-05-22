import markdown
from django.conf import settings
from django.db import models

USER = settings.AUTH_USER_MODEL

# Create your models here.


# image and user will be added later
class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    raw_content = models.TextField()

    @property
    def content(self):
        return markdown.markdown(self.raw_content, extensions=["extra"])


# image will be added later
class Question(models.Model):
    content = models.TextField()
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
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
