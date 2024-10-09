

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruitipedia.common.urls')),
    path('fruit/', include('fruitipedia.fruits.urls')),
    path('profile/', include('fruitipedia.accounts.urls')),
]
