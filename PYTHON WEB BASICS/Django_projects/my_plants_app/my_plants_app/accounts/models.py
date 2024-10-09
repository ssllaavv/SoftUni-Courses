from django.core import validators
from django.db import models
from my_plants_app.accounts.validators import validate_first_letter_capital


class Profile(models.Model):
    NAME_MAX_LEN = 20
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LEN),
        ],
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            validate_first_letter_capital,
        ]
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            validate_first_letter_capital,
        ]
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.username} : {self.first_name} {self.last_name}'
    
