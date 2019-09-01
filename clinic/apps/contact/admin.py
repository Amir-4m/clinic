#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin

from .models import Message
from .forms import MessageAdminForm


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    form = MessageAdminForm
    list_display = ['name', 'subject', 'email', 'created']
    readonly_fields = ['name', 'subject', 'email']
    # list_display_links
    # list_filter
    # ordering
    search_fields = ['name', 'subject', 'email']
    # autocomplete_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['name', 'subject', 'email']

    def has_add_permission(self, request, obj=None):
        return False
