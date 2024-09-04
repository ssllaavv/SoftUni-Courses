
from django.urls import path, include
from my_music_app.web import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('album/', include([
        path('add/', views.album_add, name='album add'),
        path('detais/<int:pk>', views.album_details, name='album details'),
        path('edit/<int:pk>', views.album_edit, name='album edit'),
        path('delete/<int:pk>', views.album_delete, name='album delete'),

    ])),
    path('profile/', include([
        path('details/', views.profile_details, name='profile details'),
        path('delete/', views.profile_delete, name='delete profile'),
    ])),
]
