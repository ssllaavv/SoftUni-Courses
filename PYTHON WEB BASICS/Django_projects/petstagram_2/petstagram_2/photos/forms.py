from django import forms

from petstagram_2.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        # fields = '__all__'
        exclude = ['user']


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo', 'user']

