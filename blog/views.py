from django.shortcuts import render
from django.views import generic
from .models import Post

# Views

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6