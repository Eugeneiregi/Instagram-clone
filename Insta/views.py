from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required





@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    comments = Comment.objects.all()
    user_profile = Profile.objects.get(user=user)
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    context = {
        "comments":comments,
        "posts": posts,
        "profiles": profiles,
        "user_profile":user_profile
    }
    return render(request, 'index.html', context)
