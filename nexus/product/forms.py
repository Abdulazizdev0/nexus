from django import forms
from .models import Product,ProductImage
from django.forms import inlineformset_factory


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

ProductImageFormSet = inlineformset_factory(Product, ProductImage, form=ProductImageForm, extra=3)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'brand','condition','status','price',]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", "placeholder": "Product title"}),
            'description': forms.Textarea(attrs={'class': "form-control", "placeholder": "description"}),
            'category': forms.Select(attrs={'class': "form-control", }),
            'brand': forms.Select(attrs={'class': "form-control"}),
            'condition': forms.Select(attrs={'class':"form-control"}),
            # 'status': forms.Select(attrs={'class': "form-control"}),
            'price': forms.NumberInput(attrs={'class': "form-control", "placeholder": "Narx"}),
        }


