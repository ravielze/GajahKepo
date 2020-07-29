from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    dob = models.DateTimeField()
    # REVIEW default png
    image = models.ImageField(default = 'default.png', upload_to='pics_storage')

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def followers(self):
        return Follow.objects.filter(followUser=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()

        img = Image.open(self.image.path)
        if ((img.height > 256) or (img.width > 256)):
            img.thumbnail((256, 256))
            img.save(self.image.path)

class Follow(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    followUser = models.ForeignKey(User, related_name="followUser", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
