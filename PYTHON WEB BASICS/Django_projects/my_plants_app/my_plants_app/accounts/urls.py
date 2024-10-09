from django.urls import path, include
from my_plants_app.accounts import views

urlpatterns = [
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('details/', views.profile_details, name='profile details'),
        path('delete/', views.profile_delete, name='profile delete'),
    ]))
]

