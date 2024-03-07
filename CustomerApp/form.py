from django import forms
from django.db.models import fields
from django.forms import widgets
from ManagerApp.models import CustomerItems,CustomerBill

class ItemEdit(forms.ModelForm):
    class Meta:
        model=CustomerItems
        fields=['ItemName','quantity']
        widgets={'ItemName':forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                 'quantity':forms.TextInput(attrs={'class':'form-control'})}

class Check_TableORdelivery(forms.Form):
    Options = [
        ('empty','Select From List'),
        ('Table', 'Table'),
        ('HomeDelilvery', 'HomeDelilvery'),
      ]
    Select = forms.ChoiceField(label='Select', widget=forms.Select(attrs={'class':'form-control'}), choices=Options )

