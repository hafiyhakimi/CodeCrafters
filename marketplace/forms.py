from django import forms
from .models import prodProduct, prodStock

class ProductForm(forms.ModelForm):
    class Meta:
        model = prodProduct
        fields = [
            'productName',
            'productDesc',
            'productCategory',
            'productPrice',
            'productPhoto',
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Customizing widgets, adding placeholders, etc.
        self.fields['productName'].widget.attrs.update({'placeholder': 'Enter product name'})
        self.fields['productDesc'].widget.attrs.update({'placeholder': 'Enter product description'})
        self.fields['productCategory'].widget.attrs.update({'placeholder': 'Enter product category'})
        self.fields['productPrice'].widget.attrs.update({'placeholder': 'Enter product price'})
        self.fields['productPhoto'].widget.attrs.update({'placeholder': 'Upload product photo'})
        
class ProductStockForm(forms.ModelForm):
    class Meta:
        model = prodStock
        fields = ['stock']

    def __init__(self, *args, **kwargs):
        super(ProductStockForm, self).__init__(*args, **kwargs)
        self.fields['stock'].widget.attrs.update({'placeholder': 'Enter product stock'})
