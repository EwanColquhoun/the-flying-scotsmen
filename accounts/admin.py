from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Manages Users
    """
    list_filter = ('username', 'first_name', 'last_name', 'email')
    list_display = ('username', 'first_name', 'last_name', 'email', 'registered', 'message')
    search_fields = ['username', 'first_name', 'last_name', 'email']