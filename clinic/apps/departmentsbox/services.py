#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .models import Department


class DepartmentService(object):
    @staticmethod
    def get_all_departments():
        return Department.objects.filter(is_active=True)
