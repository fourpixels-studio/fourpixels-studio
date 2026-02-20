from django import forms
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField
from .models import Testimonial, Newsletter, Contact


class NewsletterForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Newsletter
        fields = ['email', 'captcha',]

    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if not captcha_value:
            raise forms.ValidationError("Please complete the captcha.")
        return captcha_value


class TestimonialForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Testimonial
        fields = [
            'name',
            'department',
            'email',
            'testimonial',
            'image',
            'post_testimonial',
            'captcha',
        ]
        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'department': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 60px;', 'placeholder': 'Enter your department, company name or position'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email (optional)'}),
            'testimonial': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 150px;', 'placeholder': 'Testimonial goes here'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'post_testimonial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['department'].required = True
        self.fields['email'].required = False
        self.fields['testimonial'].required = True
        self.fields['image'].required = False
        self.fields['post_testimonial'].required = False

    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if not captcha_value:
            raise forms.ValidationError("Please complete the captcha.")
        return captcha_value


class ContactForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ['name', 'message', 'phone_number', 'email', 'subject', 'captcha']

        def __init__(self, *args, **kwagrs):
            super(ContactForm, self).__init__(*args, **kwagrs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['message'].widget.attrs['class'] = 'form-control'
            self.fields['phone_number'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['subject'].widget.attrs['class'] = 'form-control'

    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if not captcha_value:
            raise forms.ValidationError("Please complete the captcha.")
        return captcha_value
