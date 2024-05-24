from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ["user", "gender", "age", "education", "address", "created_at"]


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "gender",
        "age",
        "address",
        "medical_college",
        "degree",
        "year_of_passing",
        "verified",
        "created_at",
    ]

    list_editable = ["verified"]
