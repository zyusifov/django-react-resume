from django.db import models
from account.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)