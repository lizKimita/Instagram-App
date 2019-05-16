from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Profile

# Create your views here.
def all_posts(request):
    image = Image.get_images()
    title = "posts"
    
    return render(request, 'all_posts/index.html', {"title":title, "image":image})