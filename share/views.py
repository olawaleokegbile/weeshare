from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Post
from .forms import PostForm, ProfileForm, CommentForm


# Create your views here.

@login_required
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)



@login_required
def new_post(request):
    #user to create a new post
    if request.method == 'POST':
        forms = PostForm(request.POST, request.FILES)
        # validate based on form validation
        if forms.is_valid():
            post = forms.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        forms = PostForm()
    context = {
        'forms': forms
    }
    return render(request, 'new_post.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('my-profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {
        'form' : form
    }
    return render(request, 'edit_profile.html', context)

@login_required
def profile_form(request):
    return render(request, 'profile.html')

@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user_profile.html', {'user': user})


@login_required
def my_post(request):
    posts = Post.objects.filter(author=request.user).order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'my_post.html', context)

def post_detail(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'posts': posts})

def delete_post(request, pk):
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
        posts.delete()
        return redirect('/')
    return render(request, 'delete_post.html')

def update_post(request, pk):
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':    
        forms = PostForm(request.POST, request.FILES, instance=posts)
        # validate based on form validation
        if forms.is_valid():
            post = forms.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        forms = PostForm(instance=posts)
    context = {
        'forms': forms
    }
    return render(request, 'update_post.html', context)

@login_required
@require_POST
def add_comment(request, post_id):
	c_form = CommentForm(request.POST)
	if c_form.is_valid():
		# pass the post id to the comment save() method which was overriden
		# in the CommentForm implementation
		comment = c_form.save(Post.objects.get(id=post_id), request.user)
	return redirect(reverse('index'))