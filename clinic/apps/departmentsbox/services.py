from .models import Department


class DepartmentService(object):
    @staticmethod
    def get_all_departments():
        return Department.objects.filter(is_active=True)
