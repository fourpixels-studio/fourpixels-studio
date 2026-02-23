from django import forms
from .models import Project, Category
from website.models import Testimonial
from django_summernote.widgets import SummernoteWidget


class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        max_length=230,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-1'})
    )
    client = forms.CharField(
        max_length=230,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-1'})
    )
    what_we_did = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control rounded-1'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control rounded-1'})
    )
    blog_link = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control rounded-1'})
    )
    image_placeholder = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control rounded-1'})
    )
    website_link = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control rounded-1'})
    )
    app_link = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control rounded-1'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control rounded-1'}),
        empty_label="Select existing category"
    )
    testimonial = forms.ModelChoiceField(
        queryset=Testimonial.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control rounded-1'}),
    )
    year = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control rounded-1', 'type': 'date'})
    )
    link_name = forms.CharField(
        max_length=230,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-1'})
    )
    company_category = forms.CharField(
        max_length=230,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-1'})
    )
    highlight = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input hover rounded-1'})
    )
    show_in_portfolio = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input hover rounded-1'})
    )
    logo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control rounded-1'})
    )
    cover = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control rounded-1'})
    )

    class Meta:
        model = Project
        fields = ("__all__")
        exclude = ['slug', 'hit_count_generic']
        widgets = {
            'content': SummernoteWidget(),
            'similar_projects': forms.SelectMultiple(attrs={'class': 'form-select', 'height': 200}),
        }
