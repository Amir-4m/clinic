#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .models import Department, DepartmentGroup


class DepartmentService(object):
    @staticmethod
    def get_all_departments():
        return Department.objects.filter(is_active=True)

    @staticmethod
    def get_all_group_departments(slug):
        return Department.objects.filter(
            is_active=True, group__slug=slug
        )

    @staticmethod
    def get_group(slug):
        return DepartmentGroup.objects.get(
            slug=slug
        )
