from blogs.models import Blog
from django.shortcuts import render
from blogs.utils import update_views
from django.shortcuts import render, get_object_or_404


def image_search(request):
    blog = get_object_or_404(Blog, pk=4)
    context = {
        'title_tag': "Search free images",
        'meta_description': blog.meta_description,
        'meta_keywords': blog.meta_keywords,
        'cover_image': blog.cover,
        'blog': blog,
    }
    update_views(request, blog)
    return render(request, 'image_search.html', context)
