from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, RegistrationForm


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You are now logged out.")
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You are now logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is not right")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request, "Great job! You've successfully registered")
            else:
                messages.error(
                    request, "We are unable to register your account")

    else:
        registration_form = RegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
