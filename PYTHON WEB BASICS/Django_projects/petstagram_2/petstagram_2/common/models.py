from django.db import models

from petstagram_2.accounts.models import PetstagramUser
from petstagram_2.photos.models import Photo


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(
        PetstagramUser,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return ''.join(self.text[:20]) + '...'

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(
        PetstagramUser,
        on_delete=models.CASCADE,
    )

