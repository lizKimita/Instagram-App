from django import forms
from .models import Image, Comments, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = []
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []