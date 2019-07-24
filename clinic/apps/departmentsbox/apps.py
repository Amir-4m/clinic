from django.conf import settings
from django.apps import AppConfig


class DepartmentsboxConfig(AppConfig):
    name = 'departmentsbox'

    def ready(self):
        if not hasattr(settings, 'DEPARTMENTSBOX_UPLOAD_TO_LOGO_DIR'):
            setattr(settings, 'DEPARTMENTSBOX_UPLOAD_TO_LOGO_DIR', 'department_logos')
