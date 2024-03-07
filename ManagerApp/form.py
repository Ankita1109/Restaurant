from django import forms


from .models import ChiefModel,Manager
from CustomerApp.models import CusDashboard,BeveragesModel,Main_CourceModel,RiceChapati,SweetCornerModel,Starter,Chinese_Snacks



class StaffForm(forms.ModelForm):
    class Meta:
        model=ChiefModel
        fields=['ChiefName','Chief_Number','Cheif_AdharCard','C_Post','Chief_Experiance','UserId','Password']
        widgets={'ChiefName':forms.TextInput(attrs={'class':'form-control'}),
                'Chief_Number':forms.TextInput(attrs={'class':'form-control'}),
                'Cheif_AdharCard':forms.TextInput(attrs={'class':'form-control'}),
                'C_Post':forms.TextInput(attrs={'class':'form-control'}),
                'Chief_Experiance':forms.TextInput(attrs={'class':'form-control'}),
                'UserId':forms.TextInput(attrs={'class':'form-control'}),
                'Password':forms.PasswordInput(attrs={'class':'form-control'})}

class Bannerfo(forms.ModelForm):
    class Meta:
        model=CusDashboard
        fields=['blockname','BannerOfdata','BannerImage']
        chooseFiled=[
                ("IceCreamCorner","IceCream Corner"),("ChocolateCorner","Chocolate Corner"),("SweetCorner","Sweet Corner"),
                ("MocktailCorner","Mocktail Corner"),("CocktailCorner","Cocktail Corner"),("VodkaCorner","Vodka Corner"),
                ("BeerCorner","Beer Corner"),("colddrinkCorner","Cold Drink Corner"),("WineCorner","Wine Corner"),
                ("AllDrinksCorner","All Drinks Corner"),("SnacksDish","Snacks Dish Corner"),("StarterMenuList","Starter Menu Corner"),
                ("ChineseDish","ChineseDish"),("ThaiMenuList","Thai Menu Corner"),("ContentailMenuList","ContentailMenuList"),("ItalianMenuList","ItalianMenuList"),
                ("VegetraianList","Vegetraian Corner"),("FoodMenuList","FoodMenuList"),("NonVegetraianList","NonVegetraianList")

            ]
        widgets={'blockname':forms.Select(choices=chooseFiled,attrs={'class':'form-control','readonly':'true'}),
                'BannerOfdata':forms.TextInput(attrs={'class':'form-control','readonly':'true'})   }
    
class BeveragesForm(forms.ModelForm):
    class Meta:
        model=BeveragesModel
        fields =['Brand','DrinkName','DrinkType','DrinkCost','DrinkImage']
        opt=(('','Select from list    ▼ '),('mocktail','mocktail'),('cocktail','cocktail'),('vodka','vodka'),('beer','beer')
                ,('wine','wine'),('colddrink','colddrink'))
        widgets={'Brand':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Brand'}),
                'DrinkName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
                'DrinkType':forms.Select( choices=opt,attrs={'class':'form-control'}),
                'DrinkCost':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cost'}) }
    
#Main cource
class MainCourceForm(forms.ModelForm):
    class Meta:
        model=Main_CourceModel
        fields=['categories','MaincourceName','MaincourceCost','Check','MaincourceIamge']
        menu_opt=(('','Select from list    ▼ '),('thai','thai'),('local','local'),('italian','italian'),('local','local'),('continenetal','continenetal'))
        check_opt=(('','Select from list    ▼ '),('veg','veg'),('nonveg','nonveg')) 
        widgets={'categories':forms.Select( choices=menu_opt,attrs={'class':'form-control'}),
                 'MaincourceName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
                 'MaincourceCost':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cost'}),
                 'Check':forms.Select( choices=check_opt,attrs={'class':'form-control'})}
#RiceChapati
class RiceChapatiForm(forms.ModelForm):
    class Meta:
        model=RiceChapati
        fields=['ItemName','ItemCost','Check','ItemImage']
        check_opt=(('','Select from list    ▼ '),('chapati','chapati'),('rice','rice'))
        widgets={'ItemName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
                    'ItemCost':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cost'}),
                    'Check':forms.Select( choices=check_opt,attrs={'class':'form-control'})}

#sweet corner
class SweetCornerModelForm(forms.ModelForm):
    class Meta:
        model=SweetCornerModel
        fields=['DessertType','DessertName','DessertCost','DessertImage']
        select_opt=(('','Select from list    ▼ '),('chocolate','chocolate'),('icecream','icecream'),('sweetdish','sweetdish'))
        widgets={'DessertName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
                'DessertCost':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cost'}),
                'DessertType':forms.Select( choices=select_opt,attrs={'class':'form-control'}) }


#Starter
class StarterForm(forms.ModelForm):
    class Meta:
        model=Starter
        fields=['categories','StarterName','Startercost','Check','starterIamge']
        check_opt=(('','Select from list    ▼ '),('veg','veg'),('nonveg','nonveg'))
        widgets={'categories':forms.Select(attrs={'class':'form-control'}),
                'StarterName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
                'Startercost':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Cost'}),
                'Check':forms.Select( choices=check_opt,attrs={'class':'form-control'}) }


#chinese &Snacks
class Chinese_SnacksForm(forms.ModelForm):
    class Meta:
        model=Chinese_Snacks
        fields=['ItemName','ItemCost','Check','ItemImage']
        check_opt=(('','Select from list    ▼ '),('snacks','snacks'),('chinese','chinese'))
        widgets={'ItemName':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Item name'}),
                'ItemCost':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Item Cost'}),
                'Check':forms.Select( choices=check_opt,attrs={'class':'form-control'}) }

#manager corner profile

class MangerProfile(forms.ModelForm):
    class Meta:
        model=Manager
        fields=["UserId","Password",'profilepic',"Name","Phone","AdharCard"]
        widgets={'UserId':forms.TextInput(attrs={'class':'form-control'}),
                'Password':forms.TextInput(attrs={'class':'form-control'}),
                
                'Name':forms.TextInput(attrs={'class':'form-control'}),
                'Phone':forms.TextInput(attrs={'class':'form-control'}),
                'AdharCard':forms.TextInput(attrs={'class':'form-control'}),
                
                }
