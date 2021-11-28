from .models import Image,Video,Pdf
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm

class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['title',]


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title',]


class PdfForm(ModelForm):
    class Meta:
        model = Pdf
        fields = ['title',]
 