from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def all_posts(request):
    image = Image.get_images()
    title = "posts"
    
    return render(request, 'all_posts/index.html', {"title":title, "image":image})