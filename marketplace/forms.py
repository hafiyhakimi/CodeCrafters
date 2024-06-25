from django import forms
from .models import prodProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = prodProduct
        fields = [
            'productName',
            'productDesc',
            'productCategory',
            'productPrice',
            'productStock',
            'productPhoto',
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Customizing widgets, adding placeholders, etc.
        self.fields['productName'].widget.attrs.update({'placeholder': 'Enter product name'})
        self.fields['productDesc'].widget.attrs.update({'placeholder': 'Enter product description'})
        self.fields['productCategory'].widget.attrs.update({'placeholder': 'Enter product category'})
        self.fields['productPrice'].widget.attrs.update({'placeholder': 'Enter product price'})
        self.fields['productStock'].widget.attrs.update({'placeholder': 'Enter product stock'})
