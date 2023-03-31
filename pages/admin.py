from django.contrib import admin
from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    list_display = ('id', 'thumbnail', 'first_name', 'last_name',
                    'designation', 'created_date')

    list_display_links = ('id', 'thumbnail', 'first_name',)

    search_fields = ('first_name', 'last_name', 'id', 'designation',)

    list_filter = ('designation',)

    def thumbnail(self, object):
        return format_html(f'<img src="{object.profile_picture.url}" width="40" style="border-radius: 50%"/>')

    thumbnail.short_description = 'Profile Picture'


admin.site.register(Team, TeamAdmin)
