from turtle import title
from django import forms
from django.forms import fields
from .models import Post

class BlogForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ['title','slug','body','created','publish','updated', 'status']  #what can be viewed in the form