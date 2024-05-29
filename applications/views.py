from blogs.models import Blog
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from PIL import Image
from django.shortcuts import render
from blogs.utils import update_views


def applications_list(request):
    context = {
        "title_tag": "Applications",
        'image_search_cover': Blog.objects.get(pk=4).cover,
        'image_compression_cover': Blog.objects.get(pk=3).cover,
    }
    return render(request, 'applications_list.html', context)


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


def image_compression(request):
    blog = get_object_or_404(Blog, pk=3)
    context = {
        'title_tag': "Easily compress images",
        'meta_description': "meta_description",
        'meta_keywords': "meta_keywords",
        'cover_image': blog.cover,
        'blog': blog,
    }
    update_views(request, blog)
    if request.method == 'POST':
        # Get the uploaded file from the request
        uploaded_file = request.FILES['image']

        file_name = uploaded_file
        # Open the uploaded image using PIL
        image = Image.open(uploaded_file)

        default_size = int(1024)
        user_size = int(request.POST.get('compression_size', default_size))

        if user_size == 512:
            selected_size = int(512)
        elif user_size == 2048:
            selected_size = int(2048)
        else:
            selected_size = default_size

        # Perform image compression
        max_image_size = selected_size  # Maximum width or height in pixels
        aspect_ratio = image.width / image.height
        new_width = int(max_image_size * aspect_ratio)
        new_height = max_image_size
        resized_image = image.resize((new_width, new_height))

        # Create a response object with the compressed image
        response = HttpResponse(content_type='image/png')
        resized_image.save(response, 'PNG')

        # Set the appropriate headers for file download
        response['Content-Disposition'] = f'attachment; filename="compressed_{file_name}.png"'

        # Add a success message to be displayed in the template
        context['success_message'] = f'The image "{file_name}" was compressed successfully! Please right-click on the image and choose "Save As" to select the download path.'
        return response

    return render(request, 'image_compression.html', context)
# Image Compression End
