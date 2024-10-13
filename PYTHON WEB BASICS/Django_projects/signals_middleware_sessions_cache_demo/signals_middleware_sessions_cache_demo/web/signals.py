from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from signals_middleware_sessions_cache_demo.web.models import Task


@receiver(pre_save, sender=Task)
def task_to_be_created(*args, **kwargs):
    print(f'You are going to create a new task: {kwargs["instance"].title}')


@receiver(post_save, sender=Task)
def task_created(*args, **kwargs):
    print(f'Task {kwargs["instance"].title} is created')

