from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="blog_update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="blog_delete"),
]
