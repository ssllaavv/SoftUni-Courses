from django.shortcuts import render, redirect

from my_music_app.web.forms import ProfileForm, AlbumForm, AlbumDeleteForm
from my_music_app.web.models import Profile, Album


def show_index(request):
    profile_exists = False
    form = ProfileForm()
    all_albums = Album.objects.all()

    if len(Profile.objects.all()) > 0:
        profile_exists = True
        context = {
            'profile_exists': profile_exists,
            'all_albums': all_albums,
        }
        return render(request, template_name='common/home-with-profile.html', context=context)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile_exists': profile_exists,
        'form': form,
    }

    return render(request, template_name='common/home-no-profile.html', context=context)


def album_add(request):
    form = AlbumForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, template_name='album/add-album.html', context=context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }

    return render(request, template_name='album/album-details.html', context=context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, template_name='album/edit-album.html', context=context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumDeleteForm(instance=album)

    if request.method == 'POST':
        form = AlbumDeleteForm(request.POST, instance=album)
        album.delete()
        return redirect('index')

    context = {
        'album': album,
        'form': form,
    }

    return render(request, template_name='album/delete-album.html', context=context)


def profile_details(request):
    profile = Profile.objects.all().first()
    albums_count = Album.objects.all().count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, template_name='profile/profile-details.html', context=context)


def profile_delete(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Album.objects.all().delete()
        return redirect('index')

    return render(request, template_name='profile/profile-delete.html')

