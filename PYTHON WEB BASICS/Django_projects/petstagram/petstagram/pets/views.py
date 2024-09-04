from django.shortcuts import render, redirect

from petstagram.common.forms import PhotoCommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm, PetDeleteForm


def details_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = PhotoCommentForm()
    context = {
        'pet':  pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, 'pet-details-page.html', context=context)


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile details', pk=1)

    context = {'form': form, }
    return render(request, 'pet-add-page.html', context=context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username, pet_slug)

    context = {'form': form}

    return render(request, 'pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect('profile details', pk=1)
    form = PetDeleteForm(instance=pet)
    context = {'form': form}

    return render(request, 'pet-delete-page.html', context=context)


