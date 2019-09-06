from django import forms

from .models import Department


class DepartmentAdminForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'descriptions', 'link', 'logo']

    def __init__(self, *args, **kwargs):
        super(DepartmentAdminForm, self).__init__(*args, **kwargs)
        self.fields['descriptions'].widget = forms.Textarea()
