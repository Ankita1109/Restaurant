from django import forms
from django.forms import fields, widgets
from ManagerApp.models import ChiefModel


class ChiefProfile(forms.ModelForm):
    class Meta:
        model=ChiefModel
        fields=['UserId','Password','ChiefName','Cheif_AdharCard','Chief_Number','ChiefAddress']
        widgets={'UserId':forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
                'Password':forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
                'ChiefName':forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
                'Cheif_AdharCard':forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
                'Chief_Number':forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
                'ChiefAddress':forms.TextInput(attrs={'class':'form-control','readonly':'True'})
                }
class ChiefProfileUpdate(forms.ModelForm):
    class Meta:
        model=ChiefModel
        fields=['UserId','Password','ChiefName','Cheif_AdharCard','Chief_Number','ChiefAddress','ProfileImage']
        widgets={'UserId':forms.TextInput(attrs={'class':'form-control'}),
                'Password':forms.TextInput(attrs={'class':'form-control'}),
                'ChiefName':forms.TextInput(attrs={'class':'form-control'}),
                'Cheif_AdharCard':forms.TextInput(attrs={'class':'form-control'}),
                'Chief_Number':forms.TextInput(attrs={'class':'form-control'}),
                'ChiefAddress':forms.TextInput(attrs={'class':'form-control'})
                }