from django.db import models

from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
