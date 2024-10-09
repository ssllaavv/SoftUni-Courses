from django.contrib import admin

from fruitipedia.fruits.models import Fruit


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass
