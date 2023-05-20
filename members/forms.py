from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class Signupform(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Signupform,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'