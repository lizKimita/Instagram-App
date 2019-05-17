from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 30)
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.CharField(max_length = 100)

    @classmethod
    def get_profile(cls):
        profile = cls.objects.all()
        return profile

    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(username__icontains=search_term)
        return profile

    def __str__(self):
        return self.profile

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        Profile.objects.filter().delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_caption = HTMLField()
    publish_date = models.DateTimeField(auto_now_add=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "editor")
    likes = models.ManyToManyField(User, blank=True, related_name = "likes")


    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return image

    def save_image(self):
        self.save()

    def delete_image(self):
        Image.objects.filter().delete()

    def update_image_caption(self, update):
        self.image_caption = update
        self.save()

    class Meta:
        ordering = ['image']


class Comments(models.Model):
    image = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "images")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_message = HTMLField()
    date_posted = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comments(cls):
        comment = cls.objects.all()
        return comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        Image.objects.filter().delete()

    def update_comment(self, update):
        self.comment_message = update
        self.save()
