from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm, BlogModelForm


def home(request):
    posts = Blog.objects.all()
    return render(request, "index.html", {"posts": posts})


# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, "new.html")


# 블로그 글을 저장해주는 함수
def create(request):
    if request.method == "POST":
        post = Blog()
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.date = timezone.now()
        post.save()
    return redirect("home")


# django formㅇㄹ 이용해서 입력값을 받는 함수
def djangonew(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data["title"]
            post.body = form.cleaned_data["body"]
            post.save()
            return redirect("home")
    else:
        form = BlogForm()
        return render(request, "djangonew.html", {"form": form})


def djangomodel(request):
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BlogModelForm()
        return render(request, "djangonew.html", {"form": form})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, "detail.html", {"blog_detail": blog_detail})
