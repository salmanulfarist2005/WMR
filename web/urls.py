from django.urls import path
from . import views
from .views import IndexView, AboutView, ServicesView, PortfolioView

app_name = 'web'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # Home Page
    path("about/", AboutView.as_view(), name="about"),  # About Page
    path("contact/", views.contact, name="contact"),  # Contact Form
    path("services/", ServicesView.as_view(), name="services"),  # Services Page
    path("portfolio/", PortfolioView.as_view(), name="portfolio"),  # Portfolio Page
]