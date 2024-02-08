from django.http import HttpResponse
from PIL import Image
from django.shortcuts import render

def image_compression(request):
    title_tag = "Easily compress images"
    
    meta_description = ""
    meta_keywords = ""
    
    context = {
        'title_tag': title_tag,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
    }
    
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

    return render(request, 'apps/image-compression.html', context)
# Image Compression End