from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Comment
from .models import Post
from .models import Category
from django.views.generic import DetailView
from .forms import CommentForm
# Create your views here.
def blog_index(request):
    index=Post.objects.all().order_by('created_on') [::-1]

    return render(request,'blog/blog_index.html',{'index':index})

def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()
            return HttpResponseRedirect(request.path)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments":comments,
        "form":form
    }

    return render(request, "blog/blog_detail.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog/blog_category.html", context)