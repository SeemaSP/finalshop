from django.conf.urls import url

from .views import Getstates, Getcities,product_list,product_detail,order_create,registration_view,coupon_apply

urlpatterns = [
    url(r'^search/states$',
        Getstates.as_view(),
        name='search-states-view'),

    url(r'^search/cities$',
        Getcities.as_view(),
        name='search-cities-view'),
    url(r'^register$',registration_view,name='register'),
    url(r'^orders/create/$',order_create,name='order_create'),
    url(r'^coupons/apply/$',coupon_apply,name='apply'),
    url(r'^$',product_list,name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',product_detail,name='product_detail'),
]
