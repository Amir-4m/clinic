from django.shortcuts import render


def show_services(request, is_amp=False):
    return render(
        request,
        'services/amp/services.html' if is_amp else 'services/services.html',
        {
            'page': 'services',
            'extend_header': True
        }
    )
