from django.urls import path
from app import views

urlpatterns = [
    path('', views.local, name='local'),
    path('local/', views.local)
]