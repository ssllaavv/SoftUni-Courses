from django import forms

from my_plants_app.plants.models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        widgets = {
            'plant_type': forms.Select(),
            'name': forms.TextInput(),
            'image_URL': forms.URLInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput()
        }


class PlantDeleteForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
