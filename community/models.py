from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

MALE = "M"
FEMALE = "F"
GENDER_CHOICES = [(MALE, "Male"), (FEMALE, "Female")]


# image will be added later
class Audience(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=MALE, null=True, blank=True
    )
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(120)], null=True, blank=True
    )
    education = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)


# image and certificates will be added later
class Doctor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(120)]
    )
    education = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    medical_college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    linkedIn = models.URLField(max_length=200)
    year_of_passing = models.DateField()
    verified = models.BooleanField(default=False)
