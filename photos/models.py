from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Topic(models.Model):
    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    created_on = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.description