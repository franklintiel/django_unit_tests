from django import forms
from .models import *
from django.contrib.auth.models import User


class Publicar_Post_form(forms.ModelForm):

    creador = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})

        )

    comentarios = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )

    correo = forms. CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )

    class Meta:
        model = Publicar_Post
        fields = ['creador', 'comentarios', 'correo']
