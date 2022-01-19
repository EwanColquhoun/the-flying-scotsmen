from django.contrib import admin
from .models import CustomUser, Group_Member


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Manages Users via the custom user model.
    """
    list_filter = ('username', 'first_name', 'last_name', 'email')
    list_display = ('username', 'first_name', 'last_name', 'email',
                    'registered', 'message')
    search_fields = ['username', 'first_name', 'last_name', 'email']


@admin.register(Group_Member)
class GroupMemberAdmin(admin.ModelAdmin):
    """
    Allows admin access to the group members.
    """

    list_filter = ('registered', 'date_joined',)
    list_display = ('user', 'registered', 'date_joined',)
    search_fields = ['user', 'registered', 'date_joined', ]
    actions = ['register_member']

    def register_member(self, queryset):
        queryset.update(registered=True)
