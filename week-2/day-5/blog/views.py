from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog_list_viewer(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request=request, template_name='home.html', context=context)
