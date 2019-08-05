#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin

from .models import Carousel, Slide


class SlideTabularInlineAdmin(admin.TabularInline):
    model = Slide

    list_display = ['title', 'preview', 'created']
    # list_display_links
    # list_filter
    ordering = ['priority']
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


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    model = Carousel
    inlines = [SlideTabularInlineAdmin]

    list_display = ['slug', 'created']
    # list_display_links
    list_filter = ['slug']
    # ordering
    search_fields = ['slug']
    # autocomplete_fields
    # readonly_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['slug']
