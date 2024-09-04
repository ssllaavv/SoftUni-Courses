from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register_user, name='profile register'),
    path('login/', views.login_user, name='profile login'),
    path('profile/<int:pk>/', include([
        path('', views.details_profile, name='profile details'),
        path('edit/', views.edit_user, name='profile edit'),
        path('delete/', views.delete_user, name='profile delete'),
    ]))
]
