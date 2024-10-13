from django.db import models
from django.contrib.auth.models import AbstractUser

from petstagram_2.accounts.validators import validate_name_is_longer_then_two_cars, validate_name_isalpha


class PetstagramUser(AbstractUser):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show')
    )

    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        max_length=30,
        validators=[
            validate_name_is_longer_then_two_cars,
            validate_name_isalpha,
        ],
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            validate_name_is_longer_then_two_cars,
            validate_name_isalpha,
        ],
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=12,
        choices=GENDER_CHOICES,
        default='Do not show',
        null=True,
        blank=True,
    )

    def get_user_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username



