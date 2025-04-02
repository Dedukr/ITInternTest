from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company
from .serializers import CompanySerializer


# Create your views here.
class CompanyView(APIView):
    def get(self, request):
        """
        GET method to retrieve all companies.
        """
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        POST method to create a new company.
        """
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        raise ValidationError(serializer.errors)
    
class CompanyDetailedView(APIView):
    def get(self, request, pk):
        """
        GET method to retrieve a single company by ID.
        """
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise NotFound(f"Company {pk} not found")
        serializer = CompanySerializer(company)
        return Response(serializer.data)
   
    def put(self, request, pk):
        """
        PUT method to update an existing company by ID.
        """
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise NotFound(f"Company {pk} not found")

        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise ValidationError(serializer.errors)
    
    def patch(self, request, pk):
        """
        PATCH method to partially update an existing company by ID.
        """
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise NotFound(f"Company {pk} not found")

        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise ValidationError(serializer.errors)

    def delete(self, request, pk):
        """
        DELETE method to delete a company by ID.
        """
        try:
            company = Company.objects.get(pk=pk)
            company.delete()
            return Response(
                {"message": "Company deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Company.DoesNotExist:
            raise NotFound(f"Company {pk} not found")
