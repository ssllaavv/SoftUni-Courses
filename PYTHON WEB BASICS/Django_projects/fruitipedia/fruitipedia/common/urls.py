from django.urls import path, include

from fruitipedia.common import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashbosrd/', views.dashboard, name='dashboard')
]