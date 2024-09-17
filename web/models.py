from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # Changed to TextField for longer descriptions
    image = models.ImageField(upload_to='portfolio_images/')
    link = models.URLField(blank=True, null=True)  # Changed to URLField for validation

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

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

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=250)
    message = models.TextField()  # Changed to TextField for longer messages

    def __str__(self):
        return self.name