from django.conf.urls import url
from .import views



urlpatterns = [
    #Shop pages
    url(r'^$', views.shop_home, name="home"),
    url(r'checkout/$', views.checkout, name="checkout"),

    # cart apis
    url(r'^cart/get/$', views.get_cart, name="cart_get"),
    url(r'^cart/add-item/$', views.add_item, name="cart_add"),
    url(r'^cart/remove-item/$', views.remove_item, name="cart_remove_item"),
    url(r'^cart/increase-quantity/$', views.increase_item_quantity, name="cart_increase_quantity"),
    url(r'^cart/decrease-quantity/$', views.decrease_item_quantity, name="cart_decrease_quantity"),
    url(r'^cart/discard/$', views.discard_cart, name="cart_discard"),
    url(r'^track-order/$', views.track_order, name="track_order"),
]
