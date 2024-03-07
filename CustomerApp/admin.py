from django.contrib import admin
from .models import BeveragesModel,SweetCornerModel,CusDashboard,MenuCategories,Starter
from .models import Main_CourceModel,RiceChapati,Chinese_Snacks

@admin.register(CusDashboard)
class DashboardBanner(admin.ModelAdmin):
    list_display=['id','blockname','dishName','DishCost','BannerOfdata','BannerImage']

# Register your models here.
@admin.register(BeveragesModel)
class BeveragesModelAdmin(admin.ModelAdmin):
    list_display=['id','DrinkName','Brand','DrinkType','DrinkCost','DrinkImage']

@admin.register(SweetCornerModel)
class SweetCornerModelAdmin(admin.ModelAdmin):
    list_display=['id','DessertName','DessertType','DessertCost','DessertImage']


#Main menu sction of restro
@admin.register(MenuCategories)
class MenuCategoriesAdmin(admin.ModelAdmin):
    list_display=['Caregories','CreatedDate']
@admin.register(Starter)
class StarterMenuAdmin(admin.ModelAdmin):
    list_display=['id','StarterName','categories','Startercost','Check','starterIamge','Starter']
@admin.register(Main_CourceModel)
class Main_CourceModelAdmin(admin.ModelAdmin):
    list_display=['id','MaincourceName','categories','MaincourceCost','Check','MaincourceIamge','Maincource']


@admin.register(RiceChapati)
class RiceChapatiAdmin(admin.ModelAdmin):
    list_display=['id','ItemName','Check','ItemCost','ItemImage','CreatedDate']



@admin.register(Chinese_Snacks)
class Chinese_SnacksAdmin(admin.ModelAdmin):
    list_display=['id','ItemName','Check','ItemCost','ItemImage','CreatedDate']
