from .views import blog_list_viewer, blog_detail_viewer
from django.urls import path

urlpatterns = [
    path("", blog_list_viewer, name='blog_list_view'),
    path("blogs/<int:id>/", blog_detail_viewer, name='blog_detail_view'),
]
