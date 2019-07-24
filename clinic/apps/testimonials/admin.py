from django.contrib import admin

from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_display = ['user_full_name', 'created_at']


admin.site.register(Testimonial, TestimonialAdmin)
