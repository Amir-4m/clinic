from django.shortcuts import render


def home(request):
    return render(
        request,
        'clinic/layout.html',
        {
            'extend_header': False
        }
    )
