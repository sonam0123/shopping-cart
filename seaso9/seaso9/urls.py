from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers

from inventory import views
from inventory.api import ProductViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/login/$', 'dashboard.views.login_user'),

    url(r'', include('shop.urls', namespace="shop")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls', namespace="dashboard")),

   #url(r'^product/$', views.product_list),
   # url(r'^product/(?P<pk>\d+)/$', views.product_details),
   # url(r'^home/(?P<pk>\d+)/$', views.productDetails),
   # url(r'^home/$', views.home),
   # url(r'^home/products/$', views.products),
   # url(r'^home/deals/$', views.Deals),
   # url(r'^home/stores/$', views.Store),
   # url(r'^home/contact/$', views.contact),
   # url(r'^home/signup/$', views.registration_form),
   # url(r'^home/profile/$', views.profile),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
