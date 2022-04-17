from django.db import models
from apps.account.models import User


class Skill(models.Model):
    name = models.TextField(verbose_name='Skill name', unique=True)


class Education(models.Model):
    name = models.TextField(verbose_name='Education name', unique=True)


class WorkExperience(models.Model):
    name = models.TextField(verbose_name='Work name', unique=True)


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill, null=True)
    education = models.ManyToManyField(Education, null=True)
    work_experience = models.ManyToManyField(WorkExperience, null=True)
    work_experience_time = models.FloatField(null=True)
