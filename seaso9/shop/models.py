import json
from time import time

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Order(models.Model):
    status_choice = (
        ('initiated', 'Initiated'),
        ('processing', 'Processing'),
        ('dispatched', 'Dispatched'),
    )
    payment_choices = (
        ('cod', 'Cash On Delievery'),
    )
    orderid = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=10, help_text='10 digit mobile number')
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(100000)],
        help_text='6 digit valid Postel code')
    status = models.CharField(max_length=20, choices=status_choice, default='initiated')
    payment_option = models.CharField(max_length=10, choices=payment_choices)
    items = models.TextField()  # json  cart items
    total_price = models.FloatField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if (not self.pk) or (not self.orderid):
            self.orderid = str(time()).replace('.', '')
        super(Order, self).save(*args, **kwargs)

    @property
    def get_items(self):
        if self.items:
            items = json.loads(self.items)
            return items
        else:
            return []
