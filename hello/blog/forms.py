from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(forms.Form):
    author=forms.CharField(
        max_length=20,
        widget=forms.TextInput
        (attrs={'class':'form-control',
                'placeholder':'Ваше имя'})
    )
    body=forms.CharField(
        widget=forms.Textarea
        (attrs={'class':'form-control',
                'placeholder':'Ваше комментарий'})
    )
