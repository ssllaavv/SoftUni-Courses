from django import forms

from my_music_app.web.models import Profile, Album
from my_music_app.web.validators import validate_gt_zero


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),
            'age': forms.NumberInput(
                attrs={'placeholder': 'Age'}
            )
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}
            ),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description'}
            ),
            'image_URL': forms.URLInput(
                attrs={'placeholder': 'Image URL'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'Price'},

            )
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        validate_gt_zero(price)
        return price


class AlbumDeleteForm(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
