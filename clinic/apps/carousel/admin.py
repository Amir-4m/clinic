from django.contrib import admin

from .models import Carousel, Slide


class SlideTabularInlineAdmin(admin.TabularInline):
    model = Slide


class CarouselAdmin(admin.ModelAdmin):
    model = Carousel
    inlines = [SlideTabularInlineAdmin]


admin.site.register(Carousel, CarouselAdmin)
