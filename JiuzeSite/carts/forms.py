from django import forms


from orders.models import ProductPurchase


class TokenForm(forms.ModelForm):
    """
    User-related CRUD form
    """
    class Meta:
        model = ProductPurchase
        fields = [
            'order_id',
            'client_id',
            'billing_profile',
            'product',
            'my_points'
        ]

