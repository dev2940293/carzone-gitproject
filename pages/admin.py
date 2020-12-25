from django.contrib import admin
from pages.models import Team

# Register your models here.



class TeamAdminView(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'photo')
    list_display_links = ('first_name','id','last_name',)
    search_fields = ('first_name','designation',)
    list_filter = ('designation',)

admin.site.register(Team,TeamAdminView)
