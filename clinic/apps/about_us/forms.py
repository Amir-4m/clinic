from django import forms

from .models import Faq, Stuff


class FaqAdminForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question', 'answer']

    def __init__(self, *args, **kwargs):
        super(FaqAdminForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget = forms.Textarea()
        self.fields['answer'].widget = forms.Textarea()


class StuffAdminForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['title', 'description', 'logo']

    def __init__(self, *args, **kwargs):
        super(StuffAdminForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea()
