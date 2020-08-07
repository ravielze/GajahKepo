from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, SEX_CHOICES, STATUS_CHOICES

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=32, min_length=4, label='Username')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    dob = forms.DateField(required=False)
    bio = forms.CharField(label='Bio', max_length=100, required=False)
    sex = forms.ChoiceField(choices=SEX_CHOICES,label='Sex')
    status = forms.ChoiceField(choices=STATUS_CHOICES,label='Status')
    image = forms.ImageField(label='Profile Picture', required=False, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['dob', 'bio', 'sex', 'status', 'image']