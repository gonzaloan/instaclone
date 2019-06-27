""" User Admin Classes"""

# Django
from django.contrib import admin
# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Adming."""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    # Recibe campos por los que se quieran buscar
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'user__phone_number', 'user__username')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')
