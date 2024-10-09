from django.shortcuts import render, redirect

from my_plants_app.accounts.forms import ProfileForm, ProfileBaseForm
from my_plants_app.accounts.models import Profile
from my_plants_app.common.views import add_user_to_context
from my_plants_app.plants.models import Plant


def profile_create(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context=add_user_to_context(context))


def profile_details(request):
    plants_count = Plant.objects.all().count()
    context = {
        'plants_count': plants_count,
    }
    return render(request, 'profile-details.html', context=add_user_to_context(context))


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileBaseForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context=add_user_to_context(context))


def profile_delete(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        Plant.objects.all().delete()
        return redirect('index')

    context = {}

    return render(request, 'delete-profile.html', context=add_user_to_context(context))
