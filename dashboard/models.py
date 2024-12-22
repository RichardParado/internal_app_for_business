from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='brands')
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    hashtags = models.TextField(null=True, blank=True)
    tone = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name