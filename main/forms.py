from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = ['title', 'description', 'user', 'created_at']
        fields = ['title', 'description', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'title'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 6, 'placeholder': 'description'}),
            'created_at': forms.DateTimeInput(attrs={'class': 'form-control disabled mb-3', 'id': 'disabledTextInput'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'confirm password'}),
        }