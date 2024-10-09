from django import forms

from my_plants_app.accounts.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']






