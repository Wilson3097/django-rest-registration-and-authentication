from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import AccountAuthenticationForm, RegistrationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "users/home.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created succesfully. Login to continue')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, "users/profile.html")
