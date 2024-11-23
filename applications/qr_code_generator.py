import base64
import qrcode  # type: ignore
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def qr_code_generator(request):
    if request.method == "POST":
        # Retrieve form data from the POST request
        user_input = request.POST.get('qr_input')
        # Default name if not provided
        qr_name = request.POST.get('qr_name', "Four_Pixels_QR_Code")

        if user_input:
            try:
                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(user_input)
                qr.make(fit=True)

                # Create an image for the QR code
                img = qr.make_image(fill_color="black", back_color="white")

                # Save the image to a BytesIO object
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                buffer.seek(0)

                # Encode the image to base64 for frontend rendering
                qr_code_image = base64.b64encode(buffer.getvalue()).decode()

                # Save the QR code image and name for session-based download
                request.session['qr_code'] = buffer.getvalue().decode('latin1')
                request.session['qr_name'] = qr_name

                return JsonResponse({
                    'qr_code_image': qr_code_image,
                    'qr_name': qr_name,
                    'download_url': "/applications/download/QR-Code-Generator/",
                })
            except Exception as e:
                return JsonResponse({'error': f"Failed to generate QR code: {str(e)}"}, status=500)
        else:
            return JsonResponse({'error': 'Invalid input data'}, status=400)

    context = {
        'title_tag': "QR Code Generator",
        'meta_description': "Effortlessly create personalized QR codes and download them instantly with a few clicks.",
        'meta_keywrods': "QR, QR code, download QR, python, generate qr, generate free qr, free qr, QR Generator, free QR generator",
    }
    return render(request, 'qr_code_generator.html', context)


def download_qr_code(request):
    qr_code_data = request.session.get('qr_code')
    qr_name = request.session.get('qr_name', "QR_Code")

    if qr_code_data:
        response = HttpResponse(qr_code_data.encode('latin1'), content_type="image/png")
        response['Content-Disposition'] = f'attachment; filename="{qr_name}.png"'
        return response
    return JsonResponse({'error': 'No QR code available for download'}, status=400)
