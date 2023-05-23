from django.urls import path
from .views import api_response

urlpatterns = [
    path('',api_response,name='apipage'),
]