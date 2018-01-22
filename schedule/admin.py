# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_bootstrap_calendar.models import CalendarEvent

# Register your models here.
###Admin
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ["title", "url", "css_class", "start", "end"]
    list_filler = ["title"]

admin.site.register(CalendarEvent, CalendarEventAdmin)
