from news.models import Announcement
from django import forms


class edit_news(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class':'form-control'
            })
        }