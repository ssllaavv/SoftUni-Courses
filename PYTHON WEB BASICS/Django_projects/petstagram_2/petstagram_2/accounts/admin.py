from django.contrib import admin

from petstagram_2.accounts.models import PetstagramUser


# Register your models here.
@admin.register(PetstagramUser)
class PetstagramUserAdmin(admin.ModelAdmin):
    pass


