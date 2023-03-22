from django import forms

from shop.models import Topping

l = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
PRODUCT_QUANTITY_CHOICES = list(zip(l, map(str, l)))

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=str,
                                label='Вес, кг')
    topping = forms.ModelChoiceField(queryset=Topping.objects.filter(available=True),
                                     empty_label='Уточнить начинку по телефону',
                                     required=False,
                                     label="Начинка")
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)