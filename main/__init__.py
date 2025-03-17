from django.shortcuts import render, redirect
from django.contrib import messages
#from .models import Project, ContactMessage, BlogPost

# Home Page
def home(request):
    featured_projects = Project.objects.all().order_by('-created_at')[:3]  # Get latest 3 projects
    return render(request, "home.html", {"featured_projects": featured_projects})

# Projects Page
def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

# Contact Page
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")  # Stay on the contact page and show success message
        else:
            messages.error(request, "There was an error. Please check your input and try again.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

# Blog Page
def blog(request):
    posts = BlogPost.objects.all()
    return render(request, "blog.html", {"posts": posts})