from django.shortcuts import render, redirect

from fruitipedia.accounts.forms import ProfileCreateForm, ProfileEditForm
from fruitipedia.accounts.models import Profile
from fruitipedia.common.views import add_user_to_context
from fruitipedia.fruits.models import Fruit


def profile_crate(request):

    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context=add_user_to_context(context))


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None,  instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context=add_user_to_context(context))


def profile_details(request):
    fruits_count = Fruit.objects.all().count()
    context = {
        'fruits_count': fruits_count,
    }

    return render(request, 'details-profile.html', context=add_user_to_context(context))


def profile_delete(request):
    context = {}

    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    return render(request, 'delete-profile.html', context=add_user_to_context(context))

