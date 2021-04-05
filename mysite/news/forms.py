from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title news'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons news'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date news'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text news'
            })
        }
