from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin #restrict class based views

# Create your views here.

@login_required(login_url = "login")
def posts(request):
    blogs = Post.objects.all()
    context = {
        "post": blogs,

    }

    return render(request, "posts/posts.html", context )

def individual_posts(request, pk):
    X = Post.objects.get(id=pk)
    context = {
        "x" : X
    }
    return render(request, "posts/indposts.html", context)