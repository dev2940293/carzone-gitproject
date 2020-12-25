from django.db import models

# Create your models here.

class Teams(models.Model):
    first_name = models.CharField(max_length=100,help_text='First Name')
    last_name = models.CharField(max_length=100, help_text='Last Name')
    designation = models.CharField(max_length=100, help_text='Designation')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.CharField(max_length=200)
    twitter_link = models.CharField(max_length=200)
    google_plus_link = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)


