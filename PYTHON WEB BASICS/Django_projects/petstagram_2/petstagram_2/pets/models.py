from django.db import models
from django.template.defaultfilters import slugify

from petstagram_2.accounts.models import PetstagramUser


class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)
    user = models.ForeignKey(
        PetstagramUser,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}  -  {self.slug}'
