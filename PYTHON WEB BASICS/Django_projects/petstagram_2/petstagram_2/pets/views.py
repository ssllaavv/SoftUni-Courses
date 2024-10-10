from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram_2.common.forms import CommentForm
from petstagram_2.pets.forms import PetForm, PetDeleteForm
from petstagram_2.pets.models import Pet


@login_required
def pet_add(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile details', pk=request.user.pk)

    context = {'form': form}
    return render(request, template_name='pet-add-page.html', context=context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()
    if request.user.is_authenticated:
        all_liked_photos_by_request_user = [like.to_photo_id for like in request.user.like_set.all()]
    else:
        all_liked_photos_by_request_user = None
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'all_liked_photos_by_request_user': all_liked_photos_by_request_user,
    }

    return render(request, template_name='pet-details-page.html', context=context)


@login_required
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


@login_required
def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)
    context = {'form': form}
    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)

    return render(request, template_name='pet-delete-page.html', context=context)
