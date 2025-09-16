
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.PostList.as_view(), name='home'),  # root URL shows PostList
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]