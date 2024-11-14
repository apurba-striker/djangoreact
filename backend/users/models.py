from django.db import models

from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    # file will be uploaded to the Media_Root/Profile_image
    return f'profile_images/user_{instance.id}/{filename}'
class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to=user_directory_path, default = 'profile_images/default.jpg')
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username

# Create your models here.
