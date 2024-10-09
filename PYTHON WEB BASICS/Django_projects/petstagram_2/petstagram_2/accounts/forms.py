from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

from petstagram_2.accounts.models import PetstagramUser


class PetstagramUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password',
            }
        )
    )


class PetstagramUserEditForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password', )
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Profile Picture',
            'gender': 'Gender',
        }
