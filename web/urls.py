from django.urls import path
from .views import (
    IndexView, AboutView, portfolioitem_list, ContactView, ServicesView, 
    PortfolioView, contact, BlogView
)

app_name = 'web'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('portfolio/', portfolioitem_list, name='portfolioitem_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServicesView.as_view(), name='services'),
    path('portfolio-view/', PortfolioView.as_view(), name='portfolio'),
    path('contact-form/', contact, name='contact_form'),
    path('blog/', BlogView.as_view(), name='blog'),  # Blog URL added here
]