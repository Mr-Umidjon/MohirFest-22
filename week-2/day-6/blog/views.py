from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# Create your views here.
def blog_list_viewer(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request=request, template_name='home.html', context=context)


def blog_detail_viewer(request, id):
    blog = get_object_or_404(Blog, id=id)
    context = {
        'blog': blog,
    }
    # try:
    #     blog = Blog.objects.get(id=id)
    #     context = {
    #         'blog': blog,
    #     }
    # except Blog.DoesNotExist:
    #     raise Http404('No blog found')

    return render(request=request, template_name='blog_detail.html', context=context)


class BlogListView(ListView):
    model = Blog
    template_name = "home.html"
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_create_new.html'
    fields = ['title', 'author', 'text']


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = ['title', 'author', 'text']
    # fields = "__all__"
