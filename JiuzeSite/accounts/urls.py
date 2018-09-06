from django.conf.urls import url
from django.views.generic import RedirectView

from products.views import UserProductHistoryView
from .views import (
        AccountHomeView, 
        AccountEmailActivateView,
        UserDetailUpdateView
        )
app_name = 'accounts'
urlpatterns = [
    url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
    url(r'history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            AccountEmailActivateView.as_view(), 
            name='email-activate'),
    url(r'^email/resend-activation/$', 
            AccountEmailActivateView.as_view(), 
            name='resend-activation'),

    url(r'^accounts/$', RedirectView.as_view(url='/account')),
]

# account/email/confirm/asdfads/ -> activation view