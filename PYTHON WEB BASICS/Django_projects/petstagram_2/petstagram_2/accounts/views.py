from django.shortcuts import render


def register(request):
    return render(request, template_name='register-page.html')


def login(request):
    return render(request, template_name='login-page.html')


def show_profile_details(request, pk):
    return render(request, template_name='profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='profile-delete-page.html')
