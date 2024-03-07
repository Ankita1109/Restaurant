from django.db import models

# Create your models here.
chooseFiled=[
    ("IceCreamCorner","IceCream Corner"),("ChocolateCorner","Chocolate Corner"),("SweetCorner","Sweet Corner"),
    ("MocktailCorner","Mocktail Corner"),("CocktailCorner","Cocktail Corner"),("VodkaCorner","Vodka Corner"),
    ("BeerCorner","Beer Corner"),("colddrinkCorner","Cold Drink Corner"),("WineCorner","Wine Corner"),
    ("AllDrinksCorner","All Drinks Corner"),("SnacksDish","Snacks Dish Corner"),("StarterMenuList","Starter Menu Corner"),
    ("ChineseDish","ChineseDish"),("ThaiMenuList","Thai Menu Corner"),("ContentailMenuList","ContentailMenuList"),("ItalianMenuList","ItalianMenuList"),
    ("VegetraianList","Vegetraian Corner"),("FoodMenuList","FoodMenuList"),("NonVegetraianList","NonVegetraianList")

]
class CusDashboard(models.Model):
    blockname=models.CharField(max_length=300,choices=chooseFiled,unique=True)
    BannerOfdata=models.CharField(max_length=300)
    dishName=models.CharField(max_length=300,default='none')
    DishCost=models.CharField(max_length=100,default='0')
    BannerImage=models.FileField(upload_to="DashboardBanner/",max_length=600)


class BeveragesModel(models.Model):
    Brand=models.CharField(max_length=200,default='Local')
    DrinkName=models.CharField(max_length=200)
    DrinkType=models.CharField(max_length=200)
    DrinkCost=models.CharField(max_length=200)
    DrinkImage=models.FileField(upload_to="Beverages/",max_length=600)


class SweetCornerModel(models.Model):
    DessertType=models.CharField(max_length=200)
    DessertName=models.CharField(max_length=200)
    DessertCost=models.CharField(max_length=200)
    DessertImage=models.FileField(upload_to="Dessert/",max_length=600)


class MenuCategories(models.Model):
    Caregories=models.CharField(max_length=300,primary_key=True)
    CreatedDate=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.Caregories
class Starter(models.Model):
    categories=models.ForeignKey(MenuCategories,on_delete=models.CASCADE)
    StarterName=models.CharField(max_length=300)
    Startercost=models.CharField(max_length=300)
    starterIamge=models.FileField(upload_to="Mainmenu/Starter/",max_length=600,default='None')
    Check=models.CharField(max_length=100,default="veg")    
    Starter=models.DateTimeField(auto_now=True)

class Main_CourceModel(models.Model):
    categories=models.ForeignKey(MenuCategories,on_delete=models.CASCADE)
    MaincourceName=models.CharField(max_length=300)
    MaincourceCost=models.CharField(max_length=300)
    MaincourceIamge=models.FileField(upload_to="Mainmenu/MainCource/",max_length=600)
    Check=models.CharField(max_length=100,default="veg")    
    Maincource=models.DateTimeField(auto_now=True)


class RiceChapati(models.Model):
    ItemName=models.CharField(max_length=300,default='enter')
    ItemCost=models.CharField(max_length=100,default='0')
    ItemImage=models.FileField(upload_to="Mainmenu/RiceChapati/",max_length=600,default='None')
    Check=models.CharField(max_length=100,default="rice")
    CreatedDate=models.DateTimeField(auto_now=True)


class Chinese_Snacks(models.Model):
    ItemName=models.CharField(max_length=300)
    ItemCost=models.CharField(max_length=100)
    ItemImage=models.FileField(upload_to="Chinese_Snacks/",max_length=600,default='None')
    Check=models.CharField(max_length=100,default="snacks")
    CreatedDate=models.DateTimeField(auto_now=True)
