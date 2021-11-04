from django import forms
from .models import ProfileModel


class CreateUserProfileForms(forms.ModelForm):
    username = forms.CharField(
        label=("Username"),
        widget=forms.TextInput(attrs={
            "type": "text",
            'placeholder': 'Username',
            "class": "form-control form-control-lg",
        }),

        strip=False,
    )

    desc = forms.CharField(
        label=("Bio"),
        widget=forms.Textarea(attrs={
            "type": "text",
            'placeholder': 'Enter Bio',
            "class": "form-control form-control-lg textarea",
        }),

        strip=False,
    )
    # thumb = forms.ImageField(
    # widget=forms.ImagePreviewWidget,)

    class Meta:
        model = ProfileModel
        fields = ['username', 'desc', 'thumb']
        # thumb = forms.ImageField(widget=ImagePreviewWidget,)
        thumb = forms.ImageField(label=('thumb'), required=False, error_messages={
                                 'invalid': ("Image files only")}, widget=forms.FileInput)
