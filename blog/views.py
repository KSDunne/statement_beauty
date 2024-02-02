from django.shortcuts import render
from django.views import generic
from .models import Post

# Views
class PostList(generic.ListView):
    model = Post
