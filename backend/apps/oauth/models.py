from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'email': 'email'}

class UserManager(BaseUserManager):
    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.TextField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_veridied(self):
        "Is the user a veridied member?"
        return self.veridied

    def __str__(self):
        return self.email