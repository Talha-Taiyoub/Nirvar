from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


# image will be added later
class Audience(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    gender = models.CharField(max_length=8, null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(120)], null=True, blank=True
    )
    education = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="community/images", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now=True)


class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    gender = models.CharField(max_length=8)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(120)]
    )
    address = models.CharField(max_length=200)
    medical_college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    linkedIn = models.URLField(max_length=200)
    year_of_passing = models.DateField()
    profile_photo = models.ImageField(
        upload_to="community/images", null=True, blank=True
    )
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
