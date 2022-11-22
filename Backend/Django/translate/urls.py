from django.urls import path
from . import views

urlpatterns = [
    path('translate/<str:keyword>', views.translate),
    
]