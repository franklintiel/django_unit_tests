from django import forms
from django.contrib.auth.models import User
from .models import *


class FormPosts(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Posts
        fields = [
            'user',
            'text'
        ]
