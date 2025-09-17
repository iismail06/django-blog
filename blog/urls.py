
from django.urls import path, include
from django.contrib import admin
from blog import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.PostList.as_view(), name='home'),  # root URL shows PostList
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
]