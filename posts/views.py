from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Comments
from django.contrib.auth.decorators import login_required
from .forms import NewCommentForm, NewPostForm

# Create your views here.

def home(request):
    return render(request,'all_posts/home.html')

    
@login_required(login_url='/accounts/login/')
def feeds(request):
    image = Image.get_images()
    title = "posts"
    
    return render(request, 'all_posts/index.html', {"title":title, "image":image})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
            return redirect('allImages')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})