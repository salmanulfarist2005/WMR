# Generated by Django 5.1.1 on 2024-09-19 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_portfolioimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='slug',
        ),
    ]
