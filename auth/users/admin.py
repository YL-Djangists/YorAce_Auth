import django.contrib.admin
import django.contrib.auth.admin

import users.models


__all__ = []


@django.contrib.admin.register(users.models.UserProfile)
class UserProfileAdmin(django.contrib.admin.ModelAdmin):
    list_display = ('user', 'avatar_preview', 'last_activity')
    list_select_related = ('user',)
    search_fields = ('user__username',)
    readonly_fields = ('last_activity', 'avatar_preview')

    @django.contrib.admin.display(description='Avatar')
    def avatar_preview(self, obj):
        src = obj.avatar.url
        img = obj.avatar
        return (
            f'<img src="{src}" width="50"'
            ' style="border-radius: 5px;" />' if img else '-'
        )
