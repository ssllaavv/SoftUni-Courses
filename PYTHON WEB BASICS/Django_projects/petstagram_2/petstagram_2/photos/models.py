from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_2.accounts.models import PetstagramUser
from petstagram_2.pets.models import Pet
from petstagram_2.photos.validators import file_size_validator


USER_MODEL = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='images/',
        validators=[
            file_size_validator,
        ]
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10)
        ],
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(to=Pet, blank=True)
    date_of_publication = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date_of_publication', '-pk']

