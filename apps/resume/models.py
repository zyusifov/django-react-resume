from django.db import models
from apps.account.models import User


class Skill(models.Model):
    name = models.TextField(verbose_name='Skill name')


class Education(models.Model):
    name = models.TextField(verbose_name='Education name')


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill, null=True)
    education = models.ManyToManyField(Education, null=True)