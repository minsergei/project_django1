from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def clean_name_product(self):
        cleaned_data = self.cleaned_data.get("name_product")
        dictionary = [
            "криптовалюта",
            "казино",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for item in dictionary:
            if item in cleaned_data.lower():
                raise forms.ValidationError("Некорректное название")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get("description")
        dictionary = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for item in dictionary:
            if item in cleaned_data.lower():
                raise forms.ValidationError("Некорректное описание")
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
