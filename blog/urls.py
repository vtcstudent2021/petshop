from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path("tag/<tag>/", views.blog_tag, name="blog_tag"),
]