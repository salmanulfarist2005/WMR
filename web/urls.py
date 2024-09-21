from django.urls import path
from .views import (
    IndexView, AboutView, portfolioitem_list,  ServicesView, 
    PortfolioView, contact, BlogView,BlogDetailView,PortfolioDetailView
)

app_name = 'web'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('portfolio/', portfolioitem_list, name='portfolioitem_list'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(), name='blog-detail'),
    path('services/', ServicesView.as_view(), name='services'),
    path('portfolio-view/', PortfolioView.as_view(), name='portfolio'),
    path('contact/', contact, name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),  
    path('blog_detail/<int:id>/', PortfolioDetailView.as_view(), name='portfolio_detail'),

]