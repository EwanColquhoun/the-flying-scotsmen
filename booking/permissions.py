from .models import Booking
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Booking)
permission = Permission.objects.create(
    codename='can_join',
    name='Can Join Group',
    content_type=content_type,
)