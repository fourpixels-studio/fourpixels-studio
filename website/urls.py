from django.urls import path
from .views import *
from .account import account_login, account_logout
from .dashboard import dashboard

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path('newsletter/', newsletter, name='newsletter'),
    path('help/', help, name='help'),
    path('account/login/', account_login, name='account_login'),
    path('account/logout/', account_logout, name='account_logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('submit-testimonial/', submit_testimonial, name='submit_testimonial'),
    path('success/', success, name='success'),
]
