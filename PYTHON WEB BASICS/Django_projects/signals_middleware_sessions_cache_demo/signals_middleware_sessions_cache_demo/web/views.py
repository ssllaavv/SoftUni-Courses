import random

from django.views import generic as views
from django.contrib.auth.backends import UserModel
from django.shortcuts import render, redirect
from django.views.decorators import cache as view_cache
from django.core.cache import cache

from signals_middleware_sessions_cache_demo.web.models import Task


# @view_cache.cache_page(timeout=3)
def complete_view_cache(request):

    request.session['count'] = request.session.get('count', 0) + 1
    session_count = request.session['count']
    user = request.user
    session_dict = request.session.__dict__

    if not cache.get('users'):
        cache.set('users', UserModel.objects.all(), 30)

    users = cache.get('users')
    prev_tasks_ids = request.session.get('prev_tasks', [])

    context = {
        'count': random.randint(1, 10000),
        'users': users,
        'session_count': session_count,
        'user': user,
        'session_dict': session_dict,
        'tasks': Task.objects.all(),
        'prev_tasks': Task.objects.filter(pk__in=prev_tasks_ids)
    }
    return render(request, 'complete_view_cache.html', context=context)


def create_task(request):
    Task.objects.create(title=f'Title {random.randint(1, 10000)}')

    return redirect('complete_view_cache')


def show_task(request, pk):
    task = Task.objects.filter(pk=pk) \
        .get()
    prev_tasks = request.session.get('prev_tasks', [])
    prev_tasks.append(task.pk)
    request.session['prev_tasks'] = prev_tasks[-3:]

    print(prev_tasks)

    return redirect('complete_view_cache')


class TaskListView(views.ListView):
    paginate_by = 5
    model = Task
    template_name = 'tasks-list.html'
