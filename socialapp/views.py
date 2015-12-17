from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from socialapp.forms import UserPostForm, UserPostCommentForm, UserLoginForm
from socialapp.models import UserPost, UserPostComment, UserProfile


@login_required
def index(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        form = UserPostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user_post = UserPost(text=text, author=request.user)
            user_post.save()
        return redirect('index')


@login_required
def post_details(request, pk):
    post = UserPost.objects.get(pk=pk)
    if request.method == 'GET':
        form = UserPostCommentForm()
        context = {
            'post': post,
            'form': form,
        }
        return render(request, 'post_details.html', context)
    elif request.method == 'POST':
        form = UserPostCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment = UserPostComment(text=text, post=post, author=request.user)
            comment.save()
        return redirect('post_details', pk=pk)


def login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            context = {
                'form': form,
                'message': 'Wrong username or password!'
            }
            return render(request, 'login.html', context)
        else:
            login(request, user)
            return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('login')


def view_profile(request):
    user = request.user;
    profile = UserProfile.objects.get(user=user)
    context = {
        'username': user.get_username(),
        'prenume': profile.prenume,
        'nume': profile.nume,
        'data_nasterii': profile.data_nasterii,
        'sex': profile.sex,
        'avatar': profile.avatar,
    }
    return render(request, 'profile.html', context)


def view_profile_payload(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user__pk=pk)
    context = {
        'username': user.username,
        'prenume': profile.prenume,
        'nume': profile.nume,
        'data_nasterii': profile.data_nasterii,
        'sex': profile.sex,
        'avatar': profile.avatar,
    }
    return render(request, 'profile.html', context)
