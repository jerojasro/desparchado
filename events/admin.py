from django.contrib import admin

from .models import Event, Organizer


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'topic', 'event_date', 'price')


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    pass
