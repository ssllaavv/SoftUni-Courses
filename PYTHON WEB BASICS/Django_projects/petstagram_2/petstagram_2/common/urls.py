from django.urls import path, include
from petstagram_2.common import views


urlpatterns = [
    path('', views.show_index, name='index'),
    path('like/<int:photo_pk>', views.like_functionality, name='like'),
    path('share/<int:photo_pk>', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_pk>/', views.add_comment, name='comment')
]
