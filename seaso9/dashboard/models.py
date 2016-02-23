from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=140)
    gender = models.CharField(max_length=140)
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

