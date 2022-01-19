from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f"<img src={obj.car_photo.url} width='40' style='border-radius:50px'/>")
    thumbnail.short_description = 'car image'
    list_display = ['id', 'thumbnail', 'car_title', 'city', 'colour', 'model',
                    'year', 'body_style', 'fuel_type', 'is_featured']

    list_display_links = ['id', 'thumbnail', 'car_title', ]

    list_editable = ['is_featured', ]

    search_fields = ['car_title', 'city', 'year']

    list_filter = ['city', 'fuel_type']


admin.site.register(Car, CarAdmin)
