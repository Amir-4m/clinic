from django.contrib import admin

from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ['title']


admin.site.register(Department, DepartmentAdmin)
