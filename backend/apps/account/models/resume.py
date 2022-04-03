from django.db import models
from .user import User
from .skill import Skill


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill, blank=True)
    education = models.TextField()
    is_priority = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.user.email