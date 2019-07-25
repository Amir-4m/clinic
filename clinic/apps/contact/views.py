from django.shortcuts import render

from .forms import MessageForm


def show_contact(request, is_amp=False):
    form = MessageForm()
    if request.method.lower() == 'post':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
    return render(
        request,
        'contact/amp/contact.html' if is_amp else 'contact/contact.html',
        {
            'page': 'Contact',
            'extend_header': True,
            'form': form
        }
    )
