from django.urls import path
from .views import *
from .account import account_login, account_logout

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("blog/<slug:slug>/", blog_detail, name="blog_detail"),
    path("blogs/", blog_list, name="blog_list"),
    path('newsletter/', newsletter, name='newsletter'),
    path('testimonials/', testimonials_list, name='testimonials_list'),
    path('help/', help, name='help'),
    path('account/login/', account_login, name='account_login'),
    path('account/logout/', account_logout, name='account_logout'),
]
