from .models import ShippingAddress
from django import forms

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))

    shipping_phone = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    shipping_email = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    shipping_address1 = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 1'})
    )

    shipping_address2 = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2'}), required=False)
    shipping_city = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))

    shipping_zipcode = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}), required=False)
    shipping_country = forms.CharField(
        label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['user']
