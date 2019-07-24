from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=250)
    logo = models.ImageField(
        upload_to=getattr(settings, 'DEPARTMENTSBOX_UPLOAD_TO_LOGO_DIR', 'department_logos')
    )
    is_active = models.BooleanField(default=True)
