from django import forms

from fruitipedia.accounts.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['age', 'image_URL']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "First Name",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'helptext': "*Password length requirements: 8 to 20 characters",
                }
            ),
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }
        help_texts = {
            'password': '"*Password length requirements: 8 to 20 characters"'
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['email', 'password']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'image_URL': forms.URLInput(),
            'age': forms.NumberInput(),

        }
