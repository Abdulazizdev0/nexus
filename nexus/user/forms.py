from django import  forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}))


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Firstname"}))
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control", "placeholder": "Email"}))

    class Meta:
        model = User
        fields = ['username', 'firstname', 'email', 'password1', 'password2']
        widgets = {
            'password1' : forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Password"}),
            'password2' : forms.PasswordInput(attrs={'class': "form-control", "placeholder": "Retype Password"}),
        }

    def save(self, commit=True):
        user = super().save()
        if user:
            Profile.objects.create(
                user=user,
                firstname=self.cleaned_data['firstname']
            )
        return user