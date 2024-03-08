from django import forms
from .models import GasCylinder, AgencyStock, BookGas

class GasCylinderForm(forms.ModelForm):
    class Meta:
        model = GasCylinder
        fields = ["type","brand","weight","stock_level"]  # Include all fields in the form


class AgencyStockRequestForm(forms.ModelForm):
    class Meta:
        model = AgencyStock
        fields = ["Gas","stock"]

class GasBookForm(forms.ModelForm):
    class Meta:
        model = BookGas
        fields = ["Gas"]
