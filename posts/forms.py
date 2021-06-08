from django import forms
from .models import Post
from django.contrib.auth.models import User


class FormPost(forms.ModelForm):

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Publicado por'
    )

    state = forms.BooleanField(label='Estado', required=False)

    class Meta:
        model = Post
        fields = [
            'user',
            'text_content',
            'state'
        ]
