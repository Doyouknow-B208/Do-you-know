from django.urls import path
from . import views

urlpatterns = [
    path('relativetopkeyword/<str:keyword>', views.relativetopkeyword),
    path('relativerisingkeyword/<str:keyword>', views.relativerisingkeyword),
    
]