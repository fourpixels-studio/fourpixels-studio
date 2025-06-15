from blogs.models import Blog
from .utils import update_views
from django.db.models import Max
from seo_management.models import SEO
from django.shortcuts import render, get_object_or_404


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

    context = {
        'blog': blog,
        'next_blog': next_blog,
        'title_tag': blog.title,
        'meta_url': blog.meta_url,
        'previous_blog': previous_blog,
        "meta_keywords": blog.meta_keywords,
        "meta_description": blog.meta_description,
        'meta_thumbnail': blog.get_meta_thumbnail,
        'tags': [item.strip() for item in blog.tags.split(',') if item.strip()],
    }
    update_views(request, blog)
    return render(request, 'blog_detail.html', context)


def blog_list(request):
    seo = SEO.objects.first()
    context = {
        'title_tag': "Blogs",
        'blogs': Blog.objects.order_by('-pk'),
        'meta_thumbnail': seo.meta_thumbnail.url,
        'meta_description': 'Stay informed about the latest industry trends or learn how we built specific apps. From News updates, in-depth tutorials, and step-by-step guides.',
    }
    return render(request, 'blog_list.html', context)
