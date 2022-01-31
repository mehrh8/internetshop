from django import forms


class ProductNameForm(forms.Form):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
