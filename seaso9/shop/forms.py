from django import forms

from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'email', 'mobile', 'address', 'city', 'state', 'pin', 'payment_option']
