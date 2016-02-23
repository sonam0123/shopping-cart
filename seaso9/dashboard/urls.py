from django.conf.urls import url
from .import views


urlpatterns = [

    url(r'^$', views.products_list, name="home"),
    # url(r'^signup/$', views.registration_form, name="signup"),
    # url(r'^users/$', views.userList),
    # url(r'^users/(?P<pk>[0-9]+)/update/$', views.updateuser),
    # url(r'^users/(?P<pk>[0-9]+)/delete/$', views.deleteuser),
    url(r'^login/$', views.login_user, name="login"),
    url(r'^logout/$', views.logout_user, name="logout"),

    url(r'^orders/$', views.orders_list, name="orders_list"),
    url(r'^orders/add/$', views.add_product, name="add_order"),
    url(r'^orders/(?P<id>[0-9]+)/detail/$', views.order_detail, name="order_detail"),
    url(r'^orders/(?P<id>[0-9]+)/delete/$', views.delete_order, name="order_delete"),
    url(r'^orders/(?P<id>[0-9]+)/update/$', views.update_order, name="order_update"),

    url(r'^products/$', views.products_list, name="products_list"),
    url(r'^products/add/$', views.add_product, name="add_product"),
    url(r'^products/(?P<id>[0-9]+)/delete/$', views.delete_product, name="product_delete"),
    url(r'^products/(?P<id>[0-9]+)/update/$', views.update_product, name="product_update")



]
