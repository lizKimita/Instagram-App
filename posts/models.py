from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length = 30)
    profile_photo = models.ImageField(upload_to = 'images/')
    Bio = models.CharField(max_length = 100)

    @classmethod
    def get_profile(cls):
        profile = cls.objects.all()
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
    image_caption = models.CharField(max_length = 30)
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
        ordering = ['image']