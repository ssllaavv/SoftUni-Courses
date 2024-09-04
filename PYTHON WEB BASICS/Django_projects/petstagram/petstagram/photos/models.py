from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.common.validators import validate_file_size


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        )
    )
    description = models.TextField(
        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        all_pets = ", ".join([pet.name for pet in self.tagged_pets.all()])
        return f'{self.pk} - {self.location}: {all_pets}'
