from django.core import validators
from django.db import models

from fruitipedia.accounts.models import Profile
from fruitipedia.fruits.validators import validate_fruit_name_contains_only_letters


class Fruit(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2
    UNIQUE_CONSTRAINT_MESSAGE = "This fruit name is already in use! Try a new one."

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(NAME_MIN_LEN),
            validate_fruit_name_contains_only_letters,
        ],
        blank=False,
        null=False,
        unique=True,
        error_messages={
            'unique': UNIQUE_CONSTRAINT_MESSAGE,
        }
    )

    image_URL = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )

    # TODO - hide owner in the form

    def __str__(self):
        return f'{self.name} - {self.description[:30] + "..."}'
