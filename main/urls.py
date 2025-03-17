from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Projects
    path("projects/", views.project_list, name="projects"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("projects/new/", views.project_create, name="project_create"),
    path("projects/<int:project_id>/edit/", views.project_update, name="project_update"),
    path("projects/<int:project_id>/delete/", views.project_delete, name="project_delete"),

    # Contact
    path("contact/", views.contact_view, name="contact"),

    # Blog
    path("blog/", views.blog_list, name="blog"),
    path("blog/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("blog/new/", views.blog_create, name="blog_create"),
    path("blog/<int:blog_id>/edit/", views.blog_update, name="blog_update"),
    path("blog/<int:blog_id>/delete/", views.blog_delete, name="blog_delete"),
]