from django.contrib import admin
from django.urls import path
from . import views
from pages.views import home

urlpatterns = [
    path('pages/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/', views.contact, name = 'contact'),
]