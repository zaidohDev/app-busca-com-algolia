from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()[:10]
    context ={
        'posts': posts
    }

    return render(request, 'app/index.html', context)


def show(request, id):
    post = Post.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'app/show.html', context)
