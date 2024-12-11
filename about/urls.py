from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),  # No as_view() here
]
