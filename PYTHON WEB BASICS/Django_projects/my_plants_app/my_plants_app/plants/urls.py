from django.urls import path, include
from my_plants_app.plants import views

urlpatterns = [
    path('create/', views.plant_create, name='plant create'),
    path('edit/<int:pk>/', views.plant_edit, name='plant edit'),
    path('details/<int:pk>/', views.plant_details, name='plant details'),
    path('delete/<int:pk>/', views.plant_delete, name='delete plant'),
]

