from django.contrib import admin
from .models import Notification
from mezzanine.conf import settings

class NotificationAdmin(admin.ModelAdmin):
	list_display = ("headline", "pub_date")
	ordering = ("pub_date",)

if settings.WINDOWS_TILE_MODEL[0] == "tile.models.Notification":
	admin.site.register(Notification, NotificationAdmin)