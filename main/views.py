from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Project, ContactMessage, BlogPost
from .forms import ContactForm

# 🚀 Home Page - Show latest 3 projects
def home(request):
    featured_projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'featured_projects': featured_projects})

# 🚀 List All Projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

# 🚀 Project Detail View
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, "project_detail.html", {"project": project})

# 🚀 Create a Project
def project_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.FILES.get("image")  # File upload
        link = request.POST.get("link")

        project = Project(title=title, description=description, image=image, link=link)
        project.save()
        messages.success(request, "Project added successfully!")
        return redirect("projects")

    return render(request, "project_form.html")

# 🚀 Update a Project
def project_update(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.title = request.POST["title"]
        project.description = request.POST["description"]
        if "image" in request.FILES:
            project.image = request.FILES["image"]
        project.link = request.POST.get("link")
        project.save()
        messages.success(request, "Project updated successfully!")
        return redirect("projects")

    return render(request, "project_form.html", {"project": project})

# 🚀 Delete a Project
def project_delete(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect("projects")

    return render(request, "project_confirm_delete.html", {"project": project})

# 🚀 Contact Form Handling
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        else:
            messages.error(request, "There was an error. Please try again.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

# 🚀 List All Blog Posts
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, "blog.html", {"posts": posts})

# 🚀 Blog Post Detail View
def blog_detail(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, "blog_detail.html", {"post": post})

# 🚀 Create a Blog Post
def blog_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]

        blog = BlogPost(title=title, content=content)
        blog.save()
        messages.success(request, "Blog post created successfully!")
        return redirect("blog")

    return render(request, "blog_form.html")

# 🚀 Update a Blog Post
def blog_update(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.save()
        messages.success(request, "Blog post updated successfully!")
        return redirect("blog")

    return render(request, "blog_form.html", {"post": post})

# 🚀 Delete a Blog Post
def blog_delete(request, blog_id):
    post = get_object_or_404(BlogPost, pk=blog_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Blog post deleted successfully!")
        return redirect("blog")

    return render(request, "blog_confirm_delete.html", {"post": post})