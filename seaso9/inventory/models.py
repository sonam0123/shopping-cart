from __future__ import unicode_literals

from django.db import models


def image_upload_path(instance, filename):
    return filename


class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    image = models.ImageField(upload_to=image_upload_path)
    description = models.CharField(max_length=225)
    stock = models.IntegerField()

    def __unicode__(self):
        return self.name

"""
user Registration

class Registration(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    """

class Cart(models.Model):
    name = models.CharField(max_length=225)
    price_per_unit = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
