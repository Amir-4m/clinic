from django.db import models
from django.utils.translation import ugettext_lazy as _


class History(models.Model):
    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Histories')

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField()
    details_link = models.URLField(blank=True, null=True)


class Faq(models.Model):
    class Meta:
        verbose_name = _('Faq')
        verbose_name_plural = _('Faqs')

    created_at = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=255)


class Stuff(models.Model):
    class Meta:
        verbose_name = _('Stuff')
        verbose_name_plural = _('Stuffs')

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    logo = models.ImageField()


class ClinicTeamMember(models.Model):
    class Meta:
        verbose_name = _('Clinic Team Member')
        verbose_name_plural = _('Clinic Team Members')

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=120)
    degree = models.CharField(max_length=80)
    avatar = models.ImageField()
