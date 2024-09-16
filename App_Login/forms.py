from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(
        required=True, 
        label="", 
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation'})
    )
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class EditProfile(forms.ModalForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'data',}))
    class Meta:
        model = UserProfile
        exclude = ('user', )