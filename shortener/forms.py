from django import forms

from .validators import validate_url, validate_dot_com


class HomeForm(forms.Form):
    url = forms.CharField(
        label='Submit URL',
        validators=[validate_url, validate_dot_com],
        widget = forms.TextInput(
            attrs = {
                'placeholder':"URL",
                'class':'form-control',
            }
        )
    )

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     return validate_url(url)