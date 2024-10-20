from django.urls import path, include
from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='pet add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_pet, name='pet details'),
        path('edit/', views.edit_pet, name='pet edit'),
        path('delete/', views.delete_pet, name='pet delete')
    ]))

]

