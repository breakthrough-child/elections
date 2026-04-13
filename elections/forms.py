from django import forms
from .models import PollingUnit, LGA

class PollingUnitForm(forms.Form):
    polling_unit = forms.ModelChoiceField(
        queryset=PollingUnit.objects.all(),
        empty_label="Select Polling Unit"
    )


class LGAForm(forms.Form):
    lga = forms.ModelChoiceField(
        queryset=LGA.objects.all(),
        empty_label="Select LGA"
    )