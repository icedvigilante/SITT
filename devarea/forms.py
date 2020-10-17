from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from .models import DevPost


class DevForm(forms.ModelForm):
    class Meta:
        model = DevPost
        fields = ('app_name', 'app_type', 'screenshot', 'snippet', 'body', 'git_hub',)

        widgets = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'app_type': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': SummernoteInplaceWidget(),
            'git_hub': forms.URLField(attrs={'class': 'form-control'})
        }
