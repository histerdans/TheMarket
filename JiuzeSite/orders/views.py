from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from carts.forms import TokenForm
from orders.models import Order, ProductPurchase


class OrderListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Order.objects.by_request(self.request).not_created()


class OrderDetailView(LoginRequiredMixin, DetailView):

    def get_object(self):
        # return Order.objects.get(id=self.kwargs.get('id'))
        # return Order.objects.get(slug=self.kwargs.get('slug'))
        qs = Order.objects.by_request(
            self.request
        ).filter(
            order_id = self.kwargs.get('order_id')
        )
        if qs.count() == 1:
            return qs.first()
        raise Http404



class LibraryView(LoginRequiredMixin, ListView):
    template_name = 'orders/library.html'
    def get_queryset(self):
        return ProductPurchase.objects.products_by_request(self.request)  # .by_request(self.request).digital()


class VerifyOwnership(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = request.GET
            product_id = request.GET.get('product_id', None)
            if product_id is not None:
                product_id = int(product_id)
                ownership_ids = ProductPurchase.objects.products_by_id(request)
                if product_id in ownership_ids:
                    return JsonResponse({'owner': True})
            return JsonResponse({'owner': False})
        raise Http404



def user_token(request):
    count = 1
    template_name = 'carts/checkout.html'
    if request.method == 'POST':

        form = TokenForm(request.POST)
        if form.is_valid() and request.user is not None:
            count = count+1
            billing_profile = request.POST.get('billing_profile', '')
            order_id = request.POST.get('order_id', '')
            client_id = request.POST.get('client_id', '')
            product = request.POST.get('product', '')
            my_points = count
            token_obj = ProductPurchase(billing_profile=billing_profile,
                                        order_id=order_id,
                                        product=product,
                                        client_id=client_id,
                                        my_points=my_points
                                        )
            token_obj.save()
            print('token updated')
            return HttpResponseRedirect(reverse('carts:success'))

    else:
        form = TokenForm()
    return render(request, template_name, {'form': form, })



