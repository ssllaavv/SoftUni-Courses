from django.urls import path, include

from fruitipedia.fruits import views

urlpatterns = [
    path('create/', views.fruit_create, name='fruit create'),
    path('<int:pk>/', include([
        path('details/', views.fruit_details, name='fruit details'),
        path('edit/', views.fruit_edit, name='edit fruit'),
        path('delete/', views.delete_fruit, name='delete fruit'),
    ])),

]
