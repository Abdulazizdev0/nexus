from django.shortcuts import render
from .models import Blog

def blog_page(request):
    blogs = Blog.objects.all()
    ctx = {
        "blogs":blogs
    }
    return render(request,'blog_pages/blog.html',ctx)
