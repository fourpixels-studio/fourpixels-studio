from django.core.mail import EmailMessage
from django.conf import settings


def send_contact_email(name, email, phone_number, message):
    email_subject = f'Message from {name}.'
    email_body = f'{message}\n\nPhone Number: {phone_number}\nEmail: {email}'
    from_email = email

    email_message = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=from_email,
        to=[settings.EMAIL_HOST_USER, settings.EMAIL_HOST_CC],
    )

    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
