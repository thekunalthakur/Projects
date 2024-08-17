from django.shortcuts import render, get_object_or_404
from .models import Project, Blog

def home(request):
    return render(request, 'portfolio/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'portfolio/blogs.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'portfolio/blog_detail.html', {'blog': blog})
