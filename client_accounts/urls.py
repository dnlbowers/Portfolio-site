from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientAccounts.as_view(), name='client_accounts'),
]
