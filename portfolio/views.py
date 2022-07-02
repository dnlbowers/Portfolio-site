from django.views.generic.base import TemplateView
from .models import Project


class PortfolioPage(TemplateView):
    """"
    View to return index page
    """
    template_name = 'portfolio/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context