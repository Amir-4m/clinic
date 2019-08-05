#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .models import Article, DescriptionTab


class ArticlesService(object):
    @staticmethod
    def get_articles():
        return Article.objects.all()


class DescriptionTabService(object):
    @staticmethod
    def get_descriptions_tabs():
        return DescriptionTab.objects.all()
