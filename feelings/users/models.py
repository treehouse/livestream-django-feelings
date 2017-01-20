from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Group(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name='%(class)s_created')
    name = models.CharField(max_length=255)
    description = models.TextField(default='')

    class Meta:
        abstract = True


class Family(Group):
    members = models.ManyToManyField(User, related_name='families')

    class Meta:
        verbose_name_plural = 'families'


class Company(Group):
    members = models.ManyToManyField(User, related_name='companies')

    class Meta:
        verbose_name_plural = 'companies'
