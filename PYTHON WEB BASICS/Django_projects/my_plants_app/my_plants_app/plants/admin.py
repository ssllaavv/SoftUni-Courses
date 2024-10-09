from django.contrib import admin

from my_plants_app.plants.models import Plant


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass
