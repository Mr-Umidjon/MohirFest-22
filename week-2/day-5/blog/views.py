from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Blog


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
