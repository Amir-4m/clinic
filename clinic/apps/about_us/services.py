#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from .models import History, Faq, Stuff, ClinicTeamMember


class AboutUsService(object):
    @staticmethod
    def get_history():
        return History.objects.last()

    @staticmethod
    def get_faqs():
        return Faq.objects.order_by('-created').all()[:3]

    @staticmethod
    def get_stuffs():
        return Stuff.objects.order_by('-created').all()[:2]

    @staticmethod
    def get_clinic_team_members():
        return ClinicTeamMember.objects.order_by('-created').all()
