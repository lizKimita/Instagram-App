from django import forms
from .models import Image, Comments, Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'publish_date','poster_id']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['date_posted', 'author', 'post_id', 'image']

   
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']