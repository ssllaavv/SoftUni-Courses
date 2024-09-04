from django.shortcuts import render
from django.shortcuts import render


def register_user(request):
    return render(request, 'register-page.html')


def login_user(request):
    return render(request, 'login-page.html')


def details_profile(request, pk):
    return render(request, 'profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'profile-edit-page.html')


def delete_user(request, pk):
    return render(request, 'profile-delete-page.html')


