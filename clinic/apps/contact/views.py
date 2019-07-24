from django.shortcuts import render


def show_contact(request, is_amp=False):
    return render(
        request,
        'contact/amp/contact.html' if is_amp else 'contact/contact.html',
        {
            'page': 'Contact',
            'extend_header': True,
        }
    )
