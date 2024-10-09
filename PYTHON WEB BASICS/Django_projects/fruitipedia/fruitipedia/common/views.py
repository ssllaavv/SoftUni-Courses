from django.shortcuts import render

from fruitipedia.accounts.models import Profile
from fruitipedia.fruits.models import Fruit


# this is not a view, but an auxiliary function for all views
def add_user_to_context(context):
    profile = Profile.objects.first()
    context['profile'] = profile
    return context


def index(request):

    context = {}

    return render(request, template_name='index.html', context=add_user_to_context(context))


def dashboard(request):
    all_fruits = Fruit.objects.all()

    context = {
        'all_fruits': all_fruits,
    }

    return render(request, template_name='dashboard.html', context=add_user_to_context(context))


