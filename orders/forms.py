from django import forms
from .models import Order

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['first_name','last_name','phone','email','address_line_1','address_line_2','country','state','city','order_note',]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'state', 'city', 'address_line_1', 'address_line_2', 'order_note','country']
        widgets = {
            'address_line_2': forms.TextInput(attrs={'required': False}),
            'order_note': forms.Textarea(attrs={'required': False}),
        }
        
