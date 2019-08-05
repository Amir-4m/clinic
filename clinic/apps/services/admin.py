#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin

from .models import Article, DescriptionTab


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ['title', 'created']
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


@admin.register(DescriptionTab)
class DescriptionTabAdmin(admin.ModelAdmin):
    model = DescriptionTab
    list_display = ['title', 'name', 'preview', 'created']
    # list_display_links
    # list_filter
    # ordering
    search_fields = ['title', 'name']
    # autocomplete_fields
    # readonly_fields
    # date_hierarchy
    exclude = []
    # fieldsets
    # paginator
    # raw_id_fields
    show_full_result_count = True
    sortable_by = ['title', 'name']
