from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from .models import UserModel
from django.views import View


class RegisterView(View):

    def get(self, request):
        return render(request, 'user/registration.html', {})

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                           first_name=form.cleaned_data['first_name'],
                           last_name=form.cleaned_data['last_name'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            my_user = UserModel(profile_photo=request.FILES['profile_photo'],
                                user=user,
                                description=request.POST['description']).save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request=request, user=user)
            return HttpResponseRedirect(f'/')
        return render(request, 'user/registration.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    template_name = 'user/logout.html'


class ProfileView(LoginRequiredMixin, View):

    def get(self, request, pk):
        profile = get_object_or_404(UserModel, pk=pk)
        return render(request, 'user/profile.html', {'profile': profile})

    def post(self, request, pk):
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        return HttpResponseRedirect(f'/user/profile/{pk}')




