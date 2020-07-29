from django.urls import path
from .views import *


urlpatterns = [
    path('add/', createProduct.as_view()),
    path('', listProduct.as_view())
]
