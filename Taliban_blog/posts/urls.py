from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name="posts"),
    path('<str:pk>/', views.individual_posts, name="indposts"),
    
]