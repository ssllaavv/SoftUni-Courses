from django.core import validators
from django.db import models

from fruitipedia.accounts.validators import name_validate_starts_with_letter


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 35
    LAST_NAME_MIN_LEN = 1
    PASS_MAX_LEN = 20
    PASS_MIN_LEN = 8
    EMAIL_MAX_LEN = 40

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            name_validate_starts_with_letter,
        ],
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            name_validate_starts_with_letter,
        ],
        blank=False,
        null=False,
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        blank=False,
        null=False,
        unique=True,
    )

    password = models.CharField(
        max_length=PASS_MAX_LEN,
        validators=[
            validators.MinLengthValidator(PASS_MIN_LEN)
        ],
        blank=False,
        null=False,
    )

    image_URL = models.URLField(
        blank=True,
        null=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=18
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.age}'
