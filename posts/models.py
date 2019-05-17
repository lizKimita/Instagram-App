from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_caption = models.CharField(max_length = 200)
    publish_date = models.DateTimeField(auto_now_add=True)


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
        ordering = ['-id']


class Comments(models.Model):
    image = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "images")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_message = models.CharField(max_length = 200)
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
