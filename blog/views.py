from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'blog/index.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

def resume(request):
    return render(request, 'blog/resume.html')

