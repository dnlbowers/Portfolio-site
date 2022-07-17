from django.views.generic.base import TemplateView


class ClientAccounts(TemplateView):
    """"
    View to return index page
    """
    template_name = 'client_accounts/client_accounts.html'
