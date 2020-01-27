from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='user_avatars/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'Профиль пользователя {self.user}'
