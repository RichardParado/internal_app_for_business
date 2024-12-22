from django import forms
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),

        }