from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from App_Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def sign_up(request):
    form =CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            # user.set_password(user.password)
            # user.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', context={'title': 'Signup', 'form': form})


def login_page(request):
    form = AuthenticationForm() #request, data=request.POST request, data=request.POST
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)#
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Posts:home'))

    return render(request, 'App_Login/login.html', context={'title': 'Login', 'form': form})        
    # return HttpResponseRedirect(reverse('App_Login:home'))

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(isinstance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(isinstance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/profile.html', context={'form': form, 'title': 'Edit Profile . Social'})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

