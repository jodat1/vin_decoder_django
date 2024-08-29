from django import forms

class VINDecoderForm(forms.Form):
    vin = forms.CharField(max_length=17, label='VIN')
