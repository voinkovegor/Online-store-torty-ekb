from django import forms


#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]
l = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
PRODUCT_QUANTITY_CHOICES = list(enumerate(map(str, l), start=1))

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=str)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

    class Meta:
        verbose_name = 'Количество'