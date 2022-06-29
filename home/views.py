from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePage(TemplateView):
    """"
    View to return index page
    """
    template_name = 'home/index.html'
    