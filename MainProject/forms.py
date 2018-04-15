from .models import AppUser
from django import forms
# from pagedown.widgets import PageDownWidget


class UserForm(forms.ModelForm):

    # description = forms.CharField(widget=PageDownWidget)

    class Meta:
        model = AppUser
        widgets = {'myfield': forms.TextInput(
            attrs={
                'class': 'form-control',
            }),
        }
        fields = [
            "name",
            'enrollmentno',
            'course',
            'year',
            'detailforappointment'
        ]
