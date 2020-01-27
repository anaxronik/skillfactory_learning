from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import *


class LoginView(View):

    def post(request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )
            if user is None:
                return HttpResponse('неправильный логин или пароль')
            if not user.is_active:
                return HttpResponse('ваш аккаунт заблокирован')
            login(request, user)
            return HttpResponse('успешный вход')
        return render(request, 'accounts/login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def test(request):
    return redirect('tasks:list')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Profile.objects.create(user=new_user)

            return render(request, 'accounts/registration_complete.html', {'new_user': new_user})
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'user_form': form})


def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form}, )
