from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ChangeProfileAvatarForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            user.profile.role = 'BU'
            user.save()
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile_home')
    else:
        signup_form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': signup_form, 'title': 'ثبت نام'})


@login_required
def profile_home(request):
    if request.method == 'POST':
        change_avatar_form = ChangeProfileAvatarForm(request.POST, request.FILES)
    return render(request, 'accounts/profile/profile_home.html')


