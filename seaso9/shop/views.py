import json
from time import strftime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import CheckoutForm
from .helpers import Cart
from inventory.models import Product
from shop.models import Order


def shop_home(request):
    return render(request, "shop/shop.html")

def get_cart(request):
    cart = Cart(request)
    cart = {'items': cart.get_cart()}
    return HttpResponse(json.dumps(cart), content_type='application/json')


def add_item(request):
    print request.POST
    print request.body
    if request.method == 'POST':
        print(request.POST)
        item_id = request.POST.get('item_id', 0)
        print(item_id)
        product =  get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart = {'items': cart.add_item(product)}
        return HttpResponse(json.dumps(cart), content_type='application/json')
    else:
        return HttpResponse(status=405)


def remove_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id', 0)
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart = {'items': cart.delete_item(product)}
        return HttpResponse(json.dumps(cart), content_type='application/json')
    else:
        return HttpResponse(status=405)


def increase_item_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id', 0)
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart = {'items': cart.increase_item_quantity(product)}
        return HttpResponse(json.dumps(cart), content_type='application/json')
    else:
        return HttpResponse(status=405)

def decrease_item_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id', 0)
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart = {'items': cart.decrease_item_quantity(product)}
        return HttpResponse(json.dumps(cart), content_type='application/json')
    else:
        return HttpResponse(status=405)


def discard_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        cart.discard_cart()
        return HttpResponse('success')
    else:
        return HttpResponse(status=405)

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cart_items = request.session.get('cart', [])
            total_price = 0
            for item in cart_items:
                total_price += item['price']
            f = form.save(commit=False)
            f.items = json.dumps(cart_items)
            f.total_price = total_price
            f.save()
            data = {
                'name': form.instance.name,
                'address': form.instance.address,
                'city': form.instance.city,
                'pin': form.instance.pin,
                'state': form.instance.state,
                'items': form.instance.get_items,
                'total_price': form.instance.total_price,
                'status': form.instance.status,
                'payment_option': form.instance.payment_option,
                'created': form.instance.created.strftime("%b %d %Y"),
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            return HttpResponse(json.dumps(form.errors), content_type='application/json')
    else:
        form = CheckoutForm()
        return render(request, 'shop/checkout_form.html', {'form': form})


def track_order(request):
    print request.GET
    print request.body
    orderid = request.GET.get('orderid', 0)
    order = get_object_or_404(Order, orderid=orderid)
    data = {
        'name': order.name,
        'address': order.address,
        'city': order.city,
        'pin': order.pin,
        'state': order.state,
        'items': order.get_items,
        'total_price': order.total_price,
        'status': order.status,
        'payment_option': order.payment_option,
        'created': order.created.strftime("%b %d %Y"),
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
