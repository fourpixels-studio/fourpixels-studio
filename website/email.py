from django.conf import settings
from django.core.mail import EmailMessage


def send_contact_email(name, subject, email, phone_number, message):
    email_body = f'{message}\n\n{name}\n{phone_number}\n{email}'
    from_email = email

    email_message = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=from_email,
        to=[settings.EMAIL_HOST_USER, settings.EMAIL_HOST_CC],
    )

    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print(f"An error occurred while sending email: {e}")


def send_testimonial_email(email, name, message_1, message_2):
    email_subject = str('Thank You for Your Testimonial!')

    email_body = f"Dear {name},\n\nI hope you're doing well.\n\nThank you so much for taking the time to write a testimonial.\n\nTestimonials like yours help others know what to expect and inspire us to continue providing the best service\n\nWarm regards,\nMoses Bartena\nVisual Identity Designer\nhello@fourpixels.studio\nFour Pixels Studio."
    from_email = settings.EMAIL_HOST_USER

    email_message = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=from_email,
        to=[email,],
    )

    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
