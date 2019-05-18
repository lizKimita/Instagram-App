from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Comments, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewCommentForm, NewPostForm, NewProfileForm
from django.core.exceptions import ObjectDoesNotExist

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
            post.profile = current_user
            post.save()
        return redirect('allImages')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = current_user
            comment.save()
        return redirect('allImages')
    else:
        form = NewCommentForm()
    return redirect(request, 'comments.html',{"form": form})


def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('NewProfile')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('NewProfile')
    else:
        form = NewProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def profile(request):
    current_user = request.user
    image = Image.objects.filter(profile = current_user)

    try:
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile.html',{ 'profile':profile,'image':image,'current_user':current_user})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)

    except ObjectDoesNotExist:
        
        raise Http404()
    return render(request,'all_posts/images.html',{'image':image})

def search_results(request):

    if 'profile' in request.GET and request.GET ["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'all_posts/search.html', {"message":message, "profiles":searched_profiles})
    else:
        message = "You haven't seached for any users yet!"
        return render(request, 'all_posts/search.html',{"message": message})

def find_profile(request,profile_id):

    try :
        profile = Profile.objects.get(id = profile_id)

    except ObjectDoesNotExist:
        
        raise Http404()

    return render(request, 'all_posts/find_profile.html', {'profile':profile})
