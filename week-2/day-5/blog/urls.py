from .views import blog_list_viewer
from django.urls import path

urlpatterns = [
    path("", blog_list_viewer, name='blog_list_view'),
]
