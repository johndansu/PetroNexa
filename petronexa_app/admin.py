from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_profile_image')

    def display_profile_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.profile_image.url)

    display_profile_image.short_description = 'Profile Image'

admin.site.register(UserProfile, UserProfileAdmin)