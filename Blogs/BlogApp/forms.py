from .models import Blogs
from django import forms
class FormBlogs(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=['title','desc','date']
