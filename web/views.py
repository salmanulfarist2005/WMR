from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView,DetailView
from .models import PortfolioItem, Portfolio, Category,Team,Client,Blog



# Index page view to list portfolio items
class IndexView(ListView):
    model = PortfolioItem
    template_name = 'web/index.html'
    
    def get_queryset(self):
        # Return the ordered queryset for PortfolioItem
        return PortfolioItem.objects.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_list'] = Team.objects.all()
        context['clients'] = Client.objects.all() 
        context['items'] = PortfolioItem.objects.all() 
        return context
    


# About page view
class AboutView(TemplateView):
    template_name = "web/about.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()  # Change 'clints' to 'clients'
        return context
    


def portfolioitem_list(request):
    return render(request, 'web/portfolioitem_list.html')


# # Contact page view
# class ContactView(TemplateView):
#     template_name = "web/contact.html"


# Services page view
class ServicesView(TemplateView):
    template_name = "web/services.html"




class PortfolioView(ListView):
    model = Portfolio
    template_name = "web/portfolio.html"
    context_object_name = 'portfolios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all categories for the filter
        context['categories'] = Category.objects.all()

        # Get the selected category from the URL
        category_slug = self.request.GET.get('category', None)

        print(f"Selected Category Slug: {category_slug}")  # Debugging: check slug

        # If a specific category is selected, filter portfolios
        if category_slug and category_slug != "All":
            try:
                category = get_object_or_404(Category, slug=category_slug)
                context['portfolios'] = Portfolio.objects.filter(category=category)
                print(f"Filtered Portfolios: {context['portfolios']}")  # Debugging: filtered portfolios
            except Category.DoesNotExist:
                # If the category is not found, show all portfolios
                context['portfolios'] = Portfolio.objects.all()
                print("Category does not exist, showing all portfolios.")
        else:
            # Show all portfolios if no category selected or 'All' is selected
            context['portfolios'] = Portfolio.objects.all()

        # Ensure context is returned after applying logic
        return context


# Contact form handling function



def contact(request):
    form = ContactForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted",
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": form.errors.as_json(),  # Displaying validation errors
            }
        return JsonResponse(response_data)
    
    context = {"is_contact": True, "form": form}
    return render(request, "web/contact.html", context)

class BlogView(TemplateView):
    template_name = 'web/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()  # Change 'clints' to 'clients'
        return context




class BlogDetailView(DetailView):
    model = Blog
    template_name = 'web/blog_detail.html'  # Assuming you have a template for blog detail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        blog = get_object_or_404(Blog, slug=slug)
        other_blogs = Blog.objects.exclude(slug=slug)
        
        context["blog"] = blog  # Single blog object
        context["other_blogs"] = other_blogs  # All other blogs except the current one

        return context
    


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'web/portfolio_detail.html' 

    def get_object(self, queryset=None):
       
        portfolio_id = self.kwargs.get('id')
        return get_object_or_404(Portfolio, id=portfolio_id)

    def get_context_data(self, **kwargs):
        # Override the context to add images to the template context
        context = super().get_context_data(**kwargs)
        
        # Assuming your Portfolio model has a method `get_images`
        portfolio = self.get_object()
        images = portfolio.get_images()  # Modify based on your actual method for fetching images
        
        context['images'] = images  # Pass the images to the template
        return context