from django.shortcuts import render


def show_about(request, is_amp=False):
    return render(
        request,
        'about_us/amp/about_us.html' if is_amp else 'about_us/about_us.html',
        {
            'page': 'About us',
            'extend_header': True,
        }
    )
