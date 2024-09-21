from django.contrib import admin
from .models import PortfolioItem,Category,Portfolio,Team,Client,Contact,Blog,PortfolioImage
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    fields = ("image",)
    extra = 1  # Number of extra empty fields to display

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]
    list_display = ('title',)
    

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug":("title",)}


