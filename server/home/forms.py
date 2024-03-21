from django import forms
from .models import User

class registerUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name','lastName', 'Email','password']