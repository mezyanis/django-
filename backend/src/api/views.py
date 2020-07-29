from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class createProduct(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class listProduct(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()