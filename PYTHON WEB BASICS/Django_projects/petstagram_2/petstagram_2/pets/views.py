from django.shortcuts import render, redirect

from petstagram_2.common.forms import CommentForm
from petstagram_2.pets.forms import PetForm, PetDeleteForm
from petstagram_2.pets.models import Pet


def pet_add(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile details', pk=1)

    context = {'form': form}
    return render(request, template_name='pet-add-page.html', context=context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form
    }

    return render(request, template_name='pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', 'doncho', pet_slug)
    context = {'form': form}

    return render(request, template_name='pet-edit-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)
    context = {'form': form}
    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)

    return render(request, template_name='pet-delete-page.html', context=context)
