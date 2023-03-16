from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'description']
        # widgets = {
        #     'first_name': forms.CharField(max_length=100),
        #     'description': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        # }