#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin

from .models import Department, DepartmentGroup
from .forms import DepartmentAdminForm


class DepartmentnlineAdmin(admin.StackedInline):
    model = Department
    form = DepartmentAdminForm
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

    extra = 1


@admin.register(DepartmentGroup)
class DepartmentGroupAdmin(admin.ModelAdmin):
    model = DepartmentGroup

    list_display = ['slug', 'title']
    fields = ['slug', 'title']
    inlines = [DepartmentnlineAdmin]
