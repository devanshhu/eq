from .models import AppUser
from django import forms
# from pagedown.widgets import PageDownWidget


class UserForm(forms.ModelForm):
    # description = forms.CharField(widget=PageDownWidget)

    class Meta:
        model = AppUser
        widgets = {'myfield': forms.TextInput(attrs={'rows': 2, 'cols': 15}), }
        fields = [
            "name",
            'enrollmentno',
            'course',
            'year',
            'timestamp'
        ]
