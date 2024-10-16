import http

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login

from petstagram_2.accounts.forms import PetstagramUserCreationForm, LoginForm, PetstagramUserEditForm
from petstagram_2.accounts.models import PetstagramUser


class UserRegisterView(views.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreationForm
    template_name = 'register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', None)

        return context

    def get_success_url(self):
        result = self.request.POST.get('next', None)
        print(result)
        if result == 'None':
            print('There is NO next!')
            return self.success_url
        return result


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login-page.html'
    next_page = reverse_lazy('index')


# @login_required
class UserLogoutView(LoginRequiredMixin, auth_views.LogoutView):
    http_method_names = ["post", "options", "get"]
    next_page = 'login'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    model = PetstagramUser
    template_name = 'profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())
        profile_image = static('images/person.png')
        if self.object.profile_picture not in ['', None]:
            profile_image = self.object.profile_picture

        context.update({
            'total_likes_count': total_likes_count,
            'profile_image': profile_image,
        })

        return context


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    model = PetstagramUser
    template_name = 'profile-delete-page.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.success_url)

