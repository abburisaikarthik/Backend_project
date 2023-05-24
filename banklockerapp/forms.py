from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'username')

class SubbankerForm(forms.ModelForm):
    class Meta:
        model = Subbanker
        fields = ('mobile',)

class LockertypeForm(forms.ModelForm):
    class Meta:
        model = Lockertype
        fields = ('type', 'price',)

