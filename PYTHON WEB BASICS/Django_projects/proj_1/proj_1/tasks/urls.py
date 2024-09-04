from django.urls import path
from proj_1.tasks import views


urlpatterns = [
    path('', views.index),
]