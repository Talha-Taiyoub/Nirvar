import markdown
from django.db import models

# Create your models here.


# image and user will be added later
class Article(models.Model):
    title = models.CharField(max_length=255)
    raw_content = models.TextField()

    @property
    def content(self):
        return markdown.markdown(self.raw_content, extensions=["extra"])
