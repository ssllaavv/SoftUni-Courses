
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_plants_app.common.urls')),
    path('', include('my_plants_app.plants.urls')),
    path('profile/', include('my_plants_app.accounts.urls')),
]
