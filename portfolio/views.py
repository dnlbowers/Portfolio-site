from django.views.generic.base import TemplateView


class PortfolioPage(TemplateView):
    """"
    View to return index page
    """
    template_name = 'portfolio/portfolio.html'