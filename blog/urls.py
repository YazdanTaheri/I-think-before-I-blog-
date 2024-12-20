from . import views
from django.urls import path, include  # Ensure include is imported

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
