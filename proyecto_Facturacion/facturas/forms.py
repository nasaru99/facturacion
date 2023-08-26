from django import forms
from .models import Factura, FacturaDetalle, Producto

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cliente', 'proveedor']

class FacturaDetalleForm(forms.ModelForm):
    class Meta:
        model = FacturaDetalle
        fields = ['producto', 'cantidad', ]

FacturaDetalleFormSet = forms.inlineformset_factory(Factura, FacturaDetalle, form=FacturaDetalleForm, extra=1)
