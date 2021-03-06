# Generated by Django 3.1.3 on 2020-12-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=100)),
                ('last_name', models.CharField(help_text='Last Name', max_length=100)),
                ('designation', models.CharField(help_text='Designation', max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('facebook_link', models.CharField(max_length=200)),
                ('twitter_link', models.CharField(max_length=200)),
                ('google_plus_link', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
