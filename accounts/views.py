from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, RegistrationForm


@login_required
def logout(request):
    """
    A message for successfully logging
    out and redirect to Index page
    """
    auth.logout(request)
    messages.success(request, "You are now logged out.")
    return redirect(reverse('index'))


def login(request):
    """
    If login credentials are authenticated,
    redirect to Index and show success message.
    If not, user is not authenticated and show
    message with invalid username or password.
    Customer needs to login to procced to checkout,
    add 'next' page as checkout.
    """
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

                if request.GET and request.GET['next'] != '/?next=/checkout/':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is not right")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """
    A view allowing users to register and shows
    messages if form is completed successfully or not
    """
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
