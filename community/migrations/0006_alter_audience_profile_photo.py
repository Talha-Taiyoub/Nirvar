# Generated by Django 5.0.6 on 2024-05-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_audience_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audience',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='community/images'),
        ),
    ]
