from django.urls import path, include
"""
URL patterns for the blog application.

- path('', views.PostList.as_view(), name='home'):
    Maps the root URL ('/') to the PostList view,
    which displays a list of blog posts.
    This uses Django's class-based view (as_view()).

- path('<slug:slug>/', views.post_detail, name='post_detail'):
    Maps URLs with a slug (e.g., '/my-post/') to the post_detail view,
    which shows details for a specific blog post.
    The 'slug' is a unique identifier for each post,
    passed as a parameter to the view.
"""
from blog import views

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.PostList.as_view(), name='home'),  # root URL shows PostList
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit,
        name='comment_edit'
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete,
        name='comment_delete'
    ),

]
