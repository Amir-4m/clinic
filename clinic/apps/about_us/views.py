from django.shortcuts import render

from .services import AboutUsService


def show_about(request, is_amp=False):
    return render(
        request,
        'about_us/amp/about_us.html' if is_amp else 'about_us/about_us.html',
        {
            'page': 'About us',
            'extend_header': True,
            'history': AboutUsService.get_history(),
            'faqs': AboutUsService.get_faqs(),
            'stuffs': AboutUsService.get_stuffs(),
            'members': AboutUsService.get_clinic_team_members()
        }
    )
