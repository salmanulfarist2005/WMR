from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# class IndexView(TemplateView):
#     template_name = 'web/index.html'


def index(request):
    return render(request,"web/index.html")