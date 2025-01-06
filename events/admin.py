from django.contrib import admin
from events.models import Event, EventRegistration

# Register your models here.
admin.site.register(Event)
admin.site.register(EventRegistration)
