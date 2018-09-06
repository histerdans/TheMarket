from django.conf.urls import url

from orders.views import user_token
from .views import (
    cart_home,
    cart_update,
    checkout_home,
    checkout_done_view)
app_name = 'carts'
urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
    url(r'^token/', user_token, name='token'),
]