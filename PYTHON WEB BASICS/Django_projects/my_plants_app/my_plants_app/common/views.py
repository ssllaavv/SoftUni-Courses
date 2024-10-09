from django.shortcuts import render

from my_plants_app.accounts.models import Profile
from my_plants_app.plants.models import Plant


def add_user_to_context(context):
    profile = Profile.objects.first()
    context['profile'] = profile
    return context


def index(request):
    context = {

    }
    return render(request, 'home-page.html', context=add_user_to_context(context))


def catalogue(request):
    all_plants = Plant.objects.all()
    context = {
        'all_plants': all_plants,
    }
    return render(request, 'catalogue.html', context=add_user_to_context(context))

