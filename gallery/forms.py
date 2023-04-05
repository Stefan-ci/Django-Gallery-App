from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placehorlder': 'monpi01',
            }
        )
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placehorlder': 'PasswordhgX@09ß',
            }
        )
    )



class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={
            'id': 'floatingInput_username',
            'class': 'form-control',
            'placeholder': 'mon_nom_01',
        })
    )
    password1 = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={
            'id': 'floatingPassword1',
            'class': 'form-control',
            'placeholder': '*************',
        })
    )
    password2 = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={
            'id': 'floatingPassword2',
            'class': 'form-control',
            'placeholder': '*************',
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
