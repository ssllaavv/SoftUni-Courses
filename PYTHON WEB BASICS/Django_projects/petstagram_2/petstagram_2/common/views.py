from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstagram_2.common.forms import CommentForm, SearchForm
from petstagram_2.common.models import Like
from petstagram_2.photos.models import Photo


def show_index(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()
    user = request.user
    if user.is_authenticated:
        all_liked_photos_by_request_user = [like.to_photo_id for like in user.like_set.all()]
    else:
        all_liked_photos_by_request_user = None

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_liked_photos_by_request_user': all_liked_photos_by_request_user,
    }

    return render(request, template_name='home-page.html', context=context)


@login_required
def like_functionality(request, photo_pk):
    photo = Photo.objects.get(pk=photo_pk)
    like_object = Like.objects.filter(to_photo_id=photo_pk, user=request.user).first()

    if like_object:
        like_object.delete()

    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_pk}")


@login_required
def copy_link_to_clipboard(request, photo_pk):
    copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_pk))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')


@login_required
def add_comment(request, photo_pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=photo_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_pk}')

