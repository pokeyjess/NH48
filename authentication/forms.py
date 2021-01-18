from django import forms
from nh48_user.models import NHUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = NHUser
        fields = ['username', 'password', 'bio', 'profile_image']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)