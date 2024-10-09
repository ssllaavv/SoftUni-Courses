from django import forms

from fruitipedia.accounts.models import Profile
from fruitipedia.fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_URL': forms.URLInput(
                attrs={
                    'placeholder': "Fruit Image URL",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': "Fruit Description",
                }
            ),
            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': "Nutrition Info",
                }
            ),
            'owner': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(FruitBaseForm, self).__init__(*args, **kwargs)
        self.fields['owner'].initial = Profile.objects.first()


class FruitCreateForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.label = ''


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
            if name == 'nutrition':
                field.widget = forms.HiddenInput()


