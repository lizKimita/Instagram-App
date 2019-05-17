from django import forms
from .models import Image, Comments

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = []
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
