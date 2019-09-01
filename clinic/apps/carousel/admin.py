#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin

from .models import Carousel, Slide


class SlideStackedInlineAdmin(admin.StackedInline):
    model = Slide

    list_display = ['title', 'preview', 'created']
    readonly_fields = ['detail_preview']
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
    inlines = [SlideStackedInlineAdmin]

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

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('slug',)
        return self.readonly_fields
