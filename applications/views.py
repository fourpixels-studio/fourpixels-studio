from blogs.models import Blog
from django.shortcuts import render


def applications_list(request):
    context = {
        "title_tag": "Applications",
        'image_search_cover': Blog.objects.get(pk=4).cover,
        'image_compression_cover': Blog.objects.get(pk=3).cover,
    }
    return render(request, 'applications_list.html', context)
