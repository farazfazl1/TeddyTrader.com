from django.contrib import admin
from .models import TeddyBear
from django.utils.html import format_html


class TeddyBearAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'name',
                    'brand', 'year', 'condition', 'price', 'is_featured',)

    list_display_links = ('id', 'thumbnail', 'name',)

    search_fields = ('id', 'name', 'brand',
                     'color', 'material', 'condition', 'year',)
    list_filter = ('city','condition', 'brand',)

    list_editable = ('is_featured',)

    def thumbnail(self, object):
        return format_html(f'<img src="{object.bear_photo.url}" width = "40" style="border-radius: 50%"/>')

    thumbnail.short_description = 'TeddyBear Photo'


# Register your models here.
admin.site.register(TeddyBear, TeddyBearAdmin)
