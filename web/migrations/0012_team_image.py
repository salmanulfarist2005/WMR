# Generated by Django 5.1.1 on 2024-09-18 04:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='team/'),
            preserve_default=False,
        ),
    ]
