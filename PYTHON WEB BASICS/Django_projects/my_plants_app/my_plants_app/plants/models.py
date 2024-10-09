from django.core import validators
from django.db import models
from my_plants_app.plants.validators import validate_name_contains_only_letters


class Plant(models.Model):
    PLANT_TYPE_MAX_LEN = 14
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2

    PLANT_CHOICES = (
        ("Outdoor", "Outdoor Plants"),
        ("Indoor", "Indoor Plants"),
    )

    plant_type = models.CharField(
        max_length=PLANT_TYPE_MAX_LEN,
        choices=PLANT_CHOICES,
        verbose_name='Type',
    )

    name = models.CharField(
        max_length=PLANT_TYPE_MAX_LEN,
        validators=[
            validators.MinLengthValidator(NAME_MIN_LEN),
            validate_name_contains_only_letters,
        ]
    )

    image_URL = models.URLField()

    description = models.TextField()

    price = models.FloatField()

    def __str__(self):
        return f'{self.name} - type: {self.plant_type} '

    class Meta:
        ordering = ['pk']


