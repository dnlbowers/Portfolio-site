from django.urls import path
from . import views

urlpatterns = [
    path('/', views.PortfolioPage.as_view(), name='portfolio'),
]