from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.

class PortfolioItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)


    def _str_(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    date = models.DateField()
    description = HTMLField()

    def _str_(self):
        return self.title


    # Assuming PortfolioImage has a ForeignKey to Portfolio with field name portfolio
    def get_images(self):
        return PortfolioImage.objects.filter(portfolio=self)


class PortfolioImage(models.Model):
    Portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    image = models.ImageField()

    def _str_(self):
        return self.image
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobil = models.CharField(max_length=15)
    service = models.CharField(max_length=250)
    message = models.TextField()  # This is fine for longer messages

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    image = models.ImageField(upload_to='team/')
    instagram_url = models.CharField(max_length=200)
    facebook_url = models.CharField(max_length=200)
    twitter_url = models.CharField(max_length=200)


    def _str_(self):
        return self.name
    

class Client(models.Model):
    image = models.ImageField(upload_to='client')
    url = models.CharField(max_length=200)




class Blog(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=250)
    detail_image = models.ImageField(upload_to='blog/')
    description = HTMLField()
    slug = models.SlugField(max_length=250,blank=True,null=True)

    def get_absolute_url(self):
        return reverse("web:blog-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
