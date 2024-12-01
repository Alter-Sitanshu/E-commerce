from django import forms

class ItemForm(forms.Form):
    item_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Item Name"
        }),
        label="Item Name"
    )
    item_desc = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.Textarea(attrs={
            "class":"form-control",
            "placeholder":"Item Desc"
        }),
        label="Description"
    )
    item_rating = forms.FloatField(
        max_value=5.0,
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":0.0
        }),
        label="Rating"
    )
    item_price = forms.FloatField(
        label="$ Price",
        widget=forms.NumberInput(attrs={
            "class":"form-control"
        })
    )
    item_image = forms.ImageField(
        required=False,
        label="Image"
    )