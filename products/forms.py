from django import forms
from .models import Comments, Products


class ProductsCreateForm:
    class Meta:
        model = Products
        fields = ('title', 'description', 'price', 'availability', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("text", "satisfaction", )
