from django.contrib import admin
from .models import CustomUser, Group_Member

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Manages Users
    """
    list_filter = ('username', 'first_name', 'last_name', 'email')
    list_display = ('username', 'first_name', 'last_name', 'email', 'message')
    search_fields = ['username', 'first_name', 'last_name', 'email']


@admin.register(Group_Member)
class Group_MemberAdmin(admin.ModelAdmin):

    list_filter = ('registered', 'date_joined',)
    list_display = ('user', 'registered', 'message', 'date_joined',)
    search_fields = ['user', 'registered', 'date_joined', ]

    def register_member(self, request, queryset):
        queryset.update(registered=True)
        
