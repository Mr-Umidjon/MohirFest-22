from .views import blog_list_viewer, blog_detail_viewer, BlogListView, BlogDetailView
from django.urls import path

urlpatterns = [
    # path("", blog_list_viewer, name='blog_list_view'),
    path("", BlogListView.as_view(), name='blog_list_view'),
    # path("blogs/<int:id>/", blog_detail_viewer, name='blog_detail_view'),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name='blog_detail_view'),
]
