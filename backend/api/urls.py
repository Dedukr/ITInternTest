from django.urls import path

from .views import CompanyDetailedView, CompanyView

urlpatterns = [
    path("companies/", CompanyView.as_view()),  # For GET (all) and POST
    path(
        "companies/<int:pk>/", CompanyDetailedView.as_view()
    ),  # For GET (by ID), PUT, DELETE
]
