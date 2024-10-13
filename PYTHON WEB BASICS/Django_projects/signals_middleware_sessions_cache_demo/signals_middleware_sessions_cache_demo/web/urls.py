from django.urls import path
from signals_middleware_sessions_cache_demo.web.signals import *

from signals_middleware_sessions_cache_demo.web.views import complete_view_cache, create_task, show_task, TaskListView

urlpatterns = [
    path('', complete_view_cache, name='complete_view_cache'),
    path('create/', create_task, name='create_task'),
    path('task/<int:pk>/', show_task, name='show_task'),
    path('tasks-list/', TaskListView.as_view(), name='list-tasks'),
]
