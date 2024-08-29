from django.shortcuts import render, get_object_or_404
from blogs.models import Blog
from .utils import update_views
from seo_management.models import SEO

seo = SEO.objects.first()


def get_previous_and_next_blog(blog):
    blogs = Blog.objects.order_by('-pub_date')
    blog_index = list(blogs).index(blog)
    previous_blog = None
    next_blog = None

    if blog_index > 0:
        previous_blog = blogs[blog_index - 1]

    if blog_index < len(blogs) - 1:
        next_blog = blogs[blog_index + 1]

    return previous_blog, next_blog


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    previous_blog, next_blog = get_previous_and_next_blog(blog)

    if blog.thumbnail:
        meta_thumbnail = blog.thumbnail.url
    else:
        meta_thumbnail = None

    context = {
        'blog': blog,
        'tags': [item.strip() for item in blog.tags.split(',') if item.strip()],
        'previous_blog': previous_blog,
        'next_blog': next_blog,
        'cover_image': blog.cover,
        'title_tag': blog.title,
        "meta_description": blog.meta_description,
        "meta_keywords": blog.meta_keywords,
        'meta_thumbnail': meta_thumbnail,
        'meta_url': blog.meta_url,
    }
    update_views(request, blog)
    return render(request, 'blog_detail.html', context)


def blog_list(request):
    context = {
        'title_tag': "Blogs",
        'blogs': Blog.objects.order_by('-pk'),
        'meta_thumbnail': seo.meta_thumbnail.url,
    }
    return render(request, 'blog_list.html', context)
