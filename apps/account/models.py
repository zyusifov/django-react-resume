from django.db import models



class User(models.Model):
    email = models.EmailField(unique=True)
    is_virified = models.BooleanField(default=False)
    password = models.CharField(max_length=255)

    @property
    def is_authenticated(self):
        """ Всегда возвращает True. Это способ узнать, был ли пользователь аутентифицированы
        """
        return True