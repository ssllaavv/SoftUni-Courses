import pyperclip
from django.shortcuts import render, redirect, resolve_url

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo
from petstagram.common.forms import PhotoCommentForm, SearchForm


def show_index(request):
    all_photos = Photo.objects.all()
    comment_form = PhotoCommentForm()
    search_form = SearchForm()

    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = Photo.objects.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(request, 'home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = PhotoLike(to_photo=photo)
        like.save()

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


def copy_link_to_clipboard(request, photo_id):
    pyperclip.copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = PhotoCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')















