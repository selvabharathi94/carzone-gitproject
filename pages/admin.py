from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f"<img src={obj.photo.url} width='40' style='border-radius:50px'/>")
    thumbnail.short_description = 'photo'
    list_display = ['id', 'thumbnail', 'first_name',
                    'last_name', 'designation', 'created_date']

    list_display_links = ['id', 'first_name', 'thumbnail']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['first_name', 'created_date']


admin.site.register(Team, TeamAdmin)
