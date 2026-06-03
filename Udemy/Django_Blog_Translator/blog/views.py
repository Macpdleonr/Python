from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

class BlogView(generic.DetailView):
  model = Post
  template_name = 'blog.html'
  context_object_name = 'post'

class AboutView(generic.TemplateView):
  template_name = 'about.html'

class PostListView(generic.ListView):
  queryset = Post.objects.filter(status=1).order_by('-date_created')
  template_name = 'index.html'