
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signals_middleware_sessions_cache_demo.web.urls')),
]
