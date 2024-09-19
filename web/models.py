from django.db import models
from django.utils import timezone

# Create your models here.

class PortfolioItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,blank=True,null=True)

    def get_Portfolio(self):
        return Portfolio.objects.filter(category=self)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='portfolio/')
    date = models.DateField()

    def __str__(self):
        return self.title
    
    def get_images(self):
        return PortfolioImage.objects.filter(Portfolio=self)

    
class PortfolioImage(models.Model):
    Portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=250)
    message = models.TextField()  # Changed to TextField for longer messages

    def __str__(self):
        return self.name
    


class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    image = models.ImageField(upload_to='team/')
    instagram_url = models.CharField(max_length=200)
    facebook_url = models.CharField(max_length=200)
    twitter_url = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    

class Client(models.Model):
    image = models.ImageField(upload_to='client')
    url = models.CharField(max_length=200)