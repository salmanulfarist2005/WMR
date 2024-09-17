# Generated by Django 5.1.1 on 2024-09-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_portfolioitem_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='portfolio_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='PortfolioItem',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='portfolio/'),
        ),
    ]
