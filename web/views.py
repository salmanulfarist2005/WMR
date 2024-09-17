from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView
from .models import PortfolioItem, Portfolio, Category


# Index page view to list portfolio items
class IndexView(ListView):
    model = PortfolioItem
    template_name = "web/index.html"
    context_object_name = 'items'

    def get_queryset(self):
        return PortfolioItem.objects.filter(is_active=True).order_by('-created_at')


# About page view
class AboutView(TemplateView):
    template_name = "web/about.html"


# Contact page view
class ContactView(TemplateView):
    template_name = "web/contact.html"


# Services page view
class ServicesView(TemplateView):
    template_name = "web/services.html"


# Portfolio page view with category filtering
class PortfolioView(ListView):
    model = Portfolio
    template_name = "web/portfolio.html"
    context_object_name = 'portfolios'

    def get_queryset(self):
        category = self.request.GET.get('category', None)
        if category:
            category_obj = get_object_or_404(Category, name=category)
            return Portfolio.objects.filter(category=category_obj)
        return Portfolio.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# Contact form handling function
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                "status": "false", 
                "title": "Form validation error",
                "errors": form.errors  # Send validation errors to frontend
            }
            return JsonResponse(response_data)
    else:
        initial_data = {'interest': 'dealership'}  # Define your initial data here
        form = ContactForm(initial=initial_data) # Pass initial data to the form
            
        context = {
            "form": form,
        }
        return render(request, "web/contact.html", context)
