# Generated by Django 5.1.1 on 2024-09-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
