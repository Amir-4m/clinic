from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    description = models.TextField()
    read_more_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.title})'


class DescriptionTab(models.Model):
    class Meta:
        verbose_name = _('Description Tab')
        verbose_name_plural = _('Description Tabs')

    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40)  # Show as tab text
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.subject} - {self.email} ({self.name})'
