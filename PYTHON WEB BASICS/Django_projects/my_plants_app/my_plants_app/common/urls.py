from django.urls import path, include

from my_plants_app.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue')
]

