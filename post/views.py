from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib import  messages
import re

post_title = '^[Aa-z]+$'

posts = Post.objects.all()
def index_view(request):
    context = {}
    posts = Post.objects.all()
    context["posts"] = posts
    if request.method == "POST":
        print(request.method)
        if request.POST["title"] != "":
            if re.match(post_title, request.POST["title"]):
                title = request.POST["title"]
                post = Post()
                post.title = title
                post.save()
                messages.success(request, "{} created ".format(title))
                return redirect('homepage')
            messages.success(request, "Python regex worked")
        messages.success(request, "White Space Not Allowd")

    return render(request, "index.html", context)

def delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('homepage')
    # if request.method == "POST":
    #     post.delete()
    #     return redirect('homepage')
    #return render(request, 'conf_delete.html')


def update_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.save()
        return redirect('homepage')
    context ={}
    context["title"] = post.title #.__len__()
    return render(request, "index.html", context)
    


