from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

STATUS_CHOICES = (('m', 'Mahasiswa'), ('d', 'Dosen'), ('a', 'Alumni'), ('s', 'Anak SMA'))
SEX_CHOICES = (('m', 'Male'), ('f', 'Female'))

class Profile(models.Model):

    def userDirectory(self, filename):
        return '{0}/{1}'.format(self.user.username, filename)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="This is a default bio.", max_length=100, null=True)
    dob = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    image = models.ImageField(default = 'default.png', upload_to=userDirectory)

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
