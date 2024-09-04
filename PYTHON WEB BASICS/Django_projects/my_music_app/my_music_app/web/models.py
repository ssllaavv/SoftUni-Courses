from django.core import validators
from django.db import models

from my_music_app.web.validators import validate_username_string


class Profile(models.Model):

    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            validators.MinLengthValidator(USERNAME_MIN_LEN),
            validate_username_string,
        ]
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.username} - {self.email}'


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30

    GENRE_CHOICES = [
        ("Pop", "Pop Music"),
        ("Jazz", "Jazz Music"),
        ("R&B", "R&B Music"),
        ("Rock", "Rock Music"),
        ("Country", "Country Music"),
        ("Dance",  "Dance Music"),
        ("Hip Hop", "Hip Hop Music"),
        ("Other", "Other"),
    ]

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
        verbose_name='Album Name'
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_URL = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(

    )

    def __str__(self):
        return f'{self.album_name} by {self.artist}'




