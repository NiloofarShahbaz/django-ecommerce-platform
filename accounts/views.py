from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST, request.FILES)
        if signup_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            user.profile.role = 'BU'
            user.profile.tel = signup_form.cleaned_data.get('tel')
            user.profile.address = signup_form.cleaned_data.get('address')
            user.profile.avatar = signup_form.cleaned_data.get('avatar')
            user.save()
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username = user.username, password=raw_password)
            login(request, user)
            return redirect('category_details', category_id=1)
    else:
        signup_form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': signup_form, 'title': 'ثبت نام'})
