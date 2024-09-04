from django.shortcuts import render
from django.http import HttpResponse
from proj_1.tasks.models import Task
from django.shortcuts import render


def index(request):
    # tasks_list = Task.objects.all()
    # output = '; '.join(f'{t.task_title}: {t.task_text}' for t in tasks_list)
    #
    # if not output:
    #     output = "There are not created tasks"
    #
    # return HttpResponse(output)

    tasks_list = Task.objects.all()
    context = {'tasks_list': tasks_list}

    return render(request, 'index.html', context)
