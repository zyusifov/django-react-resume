from django.db import models


def get_profile_path(instance, filename):
    profile_path = f'uploads/profile/user_{instance.id}.{filename.split(".")[-1]}'
    return profile_path


class User(models.Model):
    email = models.EmailField(unique=True)
    about = models.TextField(max_length=255, null=True)
    phone_no = models.IntegerField(null=True)
    is_virified = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    profile = models.ImageField(upload_to=get_profile_path, null=True)

    @property
    def is_authenticated(self):
        """ Всегда возвращает True. Это способ узнать, был ли пользователь аутентифицированы
        """
        return True


    