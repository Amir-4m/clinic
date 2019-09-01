#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin

from .models import History, Faq, Stuff, ClinicTeamMember
from .forms import FaqAdminForm, StuffAdminForm


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    model = History
    list_display = ['title', 'preview', 'created']
    readonly_fields = ['detail_preview']
    # list_display_links
    # list_filter
    # ordering
    search_fields = ['title']
    # autocomplete_fields
    # readonly_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['title']


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    model = Faq
    form = FaqAdminForm
    list_display = ['question', 'created']
    # list_display_links
    # list_filter
    # ordering
    search_fields = ['question']
    # autocomplete_fields
    # readonly_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['question']


@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    model = Stuff
    form = StuffAdminForm
    list_display = ['title', 'preview', 'created']
    readonly_fields = ['preview']
    # list_display_links
    # list_filter
    # ordering
    search_fields = ['title']
    # autocomplete_fields
    # readonly_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['title']


@admin.register(ClinicTeamMember)
class ClinicTeamMemberAdmin(admin.ModelAdmin):
    model = ClinicTeamMember
    list_display = ['name', 'degree', 'preview', 'created']
    readonly_fields = ['preview']
    # list_display_links
    # list_filter
    # ordering
    search_fields = ['name', 'degree']
    # autocomplete_fields
    # readonly_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['name']
