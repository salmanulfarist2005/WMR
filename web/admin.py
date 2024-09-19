from django.contrib import admin
from .models import PortfolioItem,Category,Portfolio,Team,Client
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('image',)