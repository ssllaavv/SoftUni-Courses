from django.urls import path, include

from petstagram_2.photos import views


urlpatterns = [
    path('add/', views.add_photo, name='photo add'),
    path('<int:pk>/', views.photo_details, name='photo details'),
    path('<int:pk>/edit', views.photo_edit, name='photo edit'),
    path('delete/<int:pk>', views.delete_photo, name='photo delete')
]