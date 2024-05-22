from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

MALE = "M"
FEMALE = "F"
GENDER_CHOICES = [(MALE, "Male"), (FEMALE, "Female")]


# image will be added later
class Audience(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(120)]
    )
    education = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


# image and certificates will be added later
class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(7), MaxValueValidator(120)]
    )
    education = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    medical_college = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    linkedIn = models.CharField(max_length=50)
    year_of_passing = models.DateField()
