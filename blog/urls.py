from .import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='home'),    # homepage
    path('<slug:slug>/', views.post_detail, name='post_detail'),    # Single post detail
  
]
