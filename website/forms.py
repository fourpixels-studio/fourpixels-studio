from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(
        max_length=50)
    last_name = forms.CharField(
        max_length=50)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

        def __init__(self, *args, **kwagrs):
            super(RegisterUserForm, self).__init__(*args, **kwagrs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs['class'] = 'form-control'
            self.fields['last_name'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ("__all__")

        def __init__(self, *args, **kwagrs):
            super(NewsletterForm, self).__init__(*args, **kwagrs)
            self.fields['customer'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ("__all__")
        exclude = ['user']

        def __init__(self, *args, **kwagrs):
            super(CustomerForm, self).__init__(*args, **kwagrs)
            self.fields['user'].widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs['class'] = 'form-control'
            self.fields['last_name'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['profile_pic'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ("__all__")
        widgets = {
            'post_testimonial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        def __init__(self, *args, **kwagrs):
            super(TestimonialForm, self).__init__(*args, **kwagrs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['department'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['image'].widget.attrs['class'] = 'form-control'
            self.fields['testimonial'].widget.attrs['class'] = 'form-control'
            



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("__all__")
        exclude = ['user']

        def __init__(self, *args, **kwagrs):
            super(ContactForm, self).__init__(*args, **kwagrs)
            self.fields['name'].widget.attrs['class'] = 'form-control'
            self.fields['message'].widget.attrs['class'] = 'form-control'
            self.fields['phone_number'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
