from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='users_profile_pic/', blank=True)

    def __str__(self):
        return f'Profile {User.username}'
