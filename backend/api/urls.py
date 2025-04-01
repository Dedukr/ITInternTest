from django.urls import path
from .views import CompanyView

urlpatterns = [
    path('companies/', CompanyView.as_view()),  # For GET (all) and POST
    path('companies/<int:pk>/', CompanyView.as_view()),  # For GET (by ID), PUT, DELETE
]